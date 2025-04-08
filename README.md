# Instrumentalizer 🎵

A powerful web application that separates vocals from instrumentals in audio files. Built with React for the frontend and Flask for the backend, this application provides an intuitive interface for processing audio files and downloading the separated tracks.

## Author

**Bennet Nkolele**  
GitHub: [@benighter](https://github.com/benighter)

## Features

- 🎵 Upload audio files in various formats (MP3, WAV)
- 🎹 Separate vocals from instrumentals using advanced audio processing
- 📊 Real-time progress tracking during processing
- ⬇️ Download individual vocal and instrumental tracks
- 💻 Modern, responsive user interface
- 🚀 Support for large audio files
- 🔄 Batch processing capabilities

## Project Structure

```
instrumentalizer/
├── backend/
│   ├── app.py              # Flask server and audio processing logic
│   ├── requirements.txt    # Python dependencies
│   ├── uploads/            # Temporary storage for uploaded files
│   └── processed/          # Storage for processed audio files
├── frontend/
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── App.js         # Main application component
│   │   └── index.js       # Application entry point
│   ├── public/            # Static assets
│   └── package.json      # Frontend dependencies
└── package.json          # Root level scripts and dependencies
```

## Prerequisites

- Node.js (v14 or higher)
- Python (v3.8 or higher)
- npm or yarn package manager
- Virtual environment for Python
- FFmpeg (for audio processing)

## Detailed Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/Benighter/Instrumentalizer.git
cd Instrumentalizer
```

### 2. Install FFmpeg

FFmpeg is required for audio processing. Install it based on your operating system:

**Windows:**
- Download from [FFmpeg website](https://ffmpeg.org/download.html)
- Add FFmpeg to your system PATH

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt update
sudo apt install ffmpeg
```

### 3. Set Up Backend

```bash
# Navigate to the backend directory
cd instrumentalizer/backend

# Create a Python virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Create necessary directories if they don't exist
mkdir uploads processed
```

### 4. Set Up Frontend

```bash
# Navigate to the frontend directory
cd ../frontend

# Install frontend dependencies
npm install

# Install additional required packages
npm install axios bootstrap @mui/material @mui/icons-material @emotion/react @emotion/styled
```

### 5. Set Up Root Level Dependencies

```bash
# Navigate back to the root directory
cd ../..

# Install root level dependencies
npm install

# Install concurrently for running both servers
npm install concurrently --save-dev
```

## Starting the Application

### Option 1: Start Both Servers Together

From the root directory:

```bash
npm start
```

This will start both the frontend and backend servers concurrently.

### Option 2: Start Servers Separately

**Start the Backend Server:**
```bash
# Navigate to the backend directory
cd instrumentalizer/backend

# Activate the virtual environment if not already activated
# On Windows:
.\venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate

# Start the Flask server
python app.py
```

The backend server will run at http://localhost:5000

**Start the Frontend Server:**
```bash
# Open a new terminal
# Navigate to the frontend directory
cd instrumentalizer/frontend

# Start the React development server
npm start
```

The frontend will run at http://localhost:3000

## Troubleshooting

### Common Issues and Solutions

1. **"No such file or directory" error when running app.py**
   - Make sure you're in the correct directory: `instrumentalizer/backend`
   - Ensure the virtual environment is activated

2. **"Missing script: start" error**
   - Make sure you're in the correct directory
   - Check that package.json exists and contains the start script
   - Run `npm install` to install dependencies

3. **Python package installation errors**
   - Try updating pip: `python -m pip install --upgrade pip`
   - For Windows users, some packages may require Visual C++ build tools
   - Try installing packages one by one to identify problematic dependencies

4. **Audio processing errors**
   - Ensure FFmpeg is installed and in your system PATH
   - Check that the uploads and processed directories exist and have write permissions

5. **CORS errors when connecting frontend to backend**
   - Verify that the backend is running on http://localhost:5000
   - Check that CORS is properly configured in the Flask app

## How to Use

1. Open your browser and navigate to `http://localhost:3000`
2. Click the "Upload" button to select an audio file
3. Once uploaded, the application will automatically begin processing
4. Track the progress in real-time through the progress bar
5. When processing is complete, download buttons will appear for:
   - Vocal track
   - Instrumental track
6. Click the respective buttons to download your separated audio files

## How It Works

Instrumentalizer uses frequency-based audio processing to separate vocals from instrumentals:

1. **Upload**: Files are securely uploaded to the backend server
2. **Processing**: The audio is analyzed using advanced signal processing techniques
3. **Separation**: Vocal and instrumental frequencies are identified and separated
4. **Download**: Processed files are made available for download

## API Endpoints

- `POST /upload` - Upload audio file
- `GET /status/<task_id>` - Check processing status
- `GET /download/<file_id>` - Download processed files

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- React.js team for the amazing frontend framework
- Flask team for the lightweight backend framework
- All contributors and users of the application

## Support

If you encounter any issues or have questions, please:
1. Check the [Issues](https://github.com/Benighter/Instrumentalizer/issues) page
2. Create a new issue if your problem isn't already listed
3. Provide as much detail as possible about your problem

---

Made with ❤️ by Bennet Nkolele 