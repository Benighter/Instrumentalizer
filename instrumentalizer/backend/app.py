import os
import uuid
import shutil
import numpy as np
import librosa
import soundfile as sf
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
ALLOWED_EXTENSIONS = {'mp3', 'wav', 'ogg', 'flac', 'aac', 'm4a'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def separate_voice_from_music(audio_file_path, vocal_file_path, instrumental_file_path):
    """
    Simple frequency-based voice separation algorithm.
    Human voice is typically in the frequency range of 80-255 Hz (men) and 165-1000 Hz (women).
    This is a basic implementation and won't work perfectly, but it's a start.
    """
    # Load audio file
    y, sr = librosa.load(audio_file_path, sr=None)
    
    # Compute Short-Time Fourier Transform
    D = librosa.stft(y)
    
    # Get magnitude and phase
    magnitude, phase = librosa.magphase(D)
    
    # Create frequency masks
    # Typical vocal frequency range (expanded for better coverage)
    vocal_mask = np.zeros_like(magnitude)
    freq_bins = librosa.fft_frequencies(sr=sr, n_fft=2048)
    
    # Approximate vocal range - adjust these values based on results
    vocal_freq_min = 200  # Hz
    vocal_freq_max = 3500  # Hz
    
    # Create a simple frequency mask (this is very basic)
    for i, freq in enumerate(freq_bins):
        if vocal_freq_min <= freq <= vocal_freq_max:
            vocal_mask[i] = 1.0
    
    # Apply masks to get vocals and instrumental
    vocal_magnitude = magnitude * vocal_mask
    instrumental_magnitude = magnitude * (1 - vocal_mask)
    
    # Reconstruct audio
    vocal_audio = librosa.istft(vocal_magnitude * phase)
    instrumental_audio = librosa.istft(instrumental_magnitude * phase)
    
    # Normalize
    vocal_audio = librosa.util.normalize(vocal_audio)
    instrumental_audio = librosa.util.normalize(instrumental_audio)
    
    # Save audio files
    sf.write(vocal_file_path, vocal_audio, sr)
    sf.write(instrumental_file_path, instrumental_audio, sr)
    
    return True

@app.route('/api/separate', methods=['POST'])
def separate_audio():
    # Check if file is in request
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    
    # Check if filename is valid
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        # Generate unique filename
        filename = secure_filename(file.filename)
        unique_id = str(uuid.uuid4())
        base_filename = os.path.splitext(filename)[0]
        file_extension = '.wav'  # We'll always output WAV for simplicity
        temp_filename = f"{base_filename}_{unique_id}{file_extension}"
        
        # Save uploaded file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], temp_filename)
        file.save(file_path)
        
        try:
            # Define output file paths
            vocals_path = os.path.join(app.config['PROCESSED_FOLDER'], f"{base_filename}_vocals_{unique_id}.wav")
            instrumental_path = os.path.join(app.config['PROCESSED_FOLDER'], f"{base_filename}_instrumental_{unique_id}.wav")
            
            # Process the audio file to separate vocals and instrumental
            separate_voice_from_music(file_path, vocals_path, instrumental_path)
            
            # Return paths to separated tracks
            output_paths = {
                'vocals': {
                    'filename': f"{base_filename}_vocals_{unique_id}.wav",
                    'path': vocals_path
                },
                'instrumental': {
                    'filename': f"{base_filename}_instrumental_{unique_id}.wav",
                    'path': instrumental_path
                }
            }
            
            return jsonify({
                'id': unique_id,
                'sources': output_paths,
                'originalName': filename
            }), 200
            
        except Exception as e:
            # Clean up on error
            if os.path.exists(file_path):
                os.remove(file_path)
            return jsonify({'error': str(e)}), 500
    
    return jsonify({'error': 'Invalid file format'}), 400

@app.route('/api/download/<filename>', methods=['GET'])
def download_file(filename):
    # Secure the filename
    filename = secure_filename(filename)
    file_path = os.path.join(app.config['PROCESSED_FOLDER'], filename)
    
    # Check if file exists
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404
    
    # Return file for download
    return send_file(file_path, as_attachment=True)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 