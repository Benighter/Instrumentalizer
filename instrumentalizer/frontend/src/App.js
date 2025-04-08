import React, { useState } from 'react';
import axios from 'axios';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const [file, setFile] = useState(null);
  const [fileName, setFileName] = useState('');
  const [processing, setProcessing] = useState(false);
  const [progress, setProgress] = useState(0);
  const [results, setResults] = useState(null);
  const [error, setError] = useState('');

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      setFileName(selectedFile.name);
      setError('');
    }
  };

  const handleDragOver = (e) => {
    e.preventDefault();
  };

  const handleDrop = (e) => {
    e.preventDefault();
    const droppedFile = e.dataTransfer.files[0];
    if (droppedFile) {
      setFile(droppedFile);
      setFileName(droppedFile.name);
      setError('');
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      setError('Please select an audio file');
      return;
    }

    setProcessing(true);
    setProgress(0);
    setResults(null);
    setError('');

    // Create a FormData object
    const formData = new FormData();
    formData.append('file', file);

    try {
      // Upload and process file with progress tracking
      const interval = setInterval(() => {
        setProgress((prevProgress) => {
          // Simulate progress up to 90% until we get actual results
          return prevProgress < 90 ? prevProgress + 5 : prevProgress;
        });
      }, 1000);

      const response = await axios.post('http://localhost:5000/api/separate', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      clearInterval(interval);
      setProgress(100);
      setResults(response.data);
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to process audio. Please try again.');
    } finally {
      setProcessing(false);
    }
  };

  const downloadFile = (filename) => {
    window.open(`http://localhost:5000/api/download/${filename}`, '_blank');
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Instrumentalizer</h1>
        <p className="subtitle">Separate vocals from instrumentals in any audio file</p>
      </header>

      <main className="container">
        <div className="row justify-content-center">
          <div className="col-md-8">
            <div className="card upload-card">
              <div className="card-body">
                <form onSubmit={handleSubmit}>
                  <div 
                    className="drop-area" 
                    onDragOver={handleDragOver}
                    onDrop={handleDrop}
                  >
                    <div className="drop-message">
                      <i className="bi bi-cloud-arrow-up-fill"></i>
                      <p>Drag & drop your audio file here</p>
                      <p className="or-text">- OR -</p>
                      <input 
                        type="file" 
                        id="file" 
                        className="file-input"
                        onChange={handleFileChange}
                        accept=".mp3,.wav,.ogg,.flac,.aac,.m4a"
                      />
                      <label htmlFor="file" className="select-button">Select File</label>
                    </div>
                    {fileName && (
                      <div className="selected-file">
                        <p>Selected: {fileName}</p>
                      </div>
                    )}
                  </div>

                  {error && <div className="alert alert-danger mt-3">{error}</div>}

                  <button 
                    type="submit" 
                    className="btn btn-primary mt-3 w-100" 
                    disabled={!file || processing}
                  >
                    {processing ? 'Processing...' : 'Separate Audio'}
                  </button>
                </form>

                {processing && (
                  <div className="progress-section mt-4">
                    <p>Processing your audio file... Please wait.</p>
                    <div className="progress">
                      <div 
                        className="progress-bar progress-bar-striped progress-bar-animated" 
                        role="progressbar" 
                        style={{ width: `${progress}%` }} 
                        aria-valuenow={progress} 
                        aria-valuemin="0" 
                        aria-valuemax="100"
                      >
                        {progress}%
                      </div>
                    </div>
                  </div>
                )}

                {results && (
                  <div className="results-section mt-4">
                    <h4>Results</h4>
                    <p>Your audio has been successfully separated!</p>
                    <div className="download-options">
                      {Object.entries(results.sources).map(([source, info]) => (
                        <div key={source} className="download-item">
                          <span className="source-name">{source.charAt(0).toUpperCase() + source.slice(1)}</span>
                          <button 
                            className="btn btn-success download-btn"
                            onClick={() => downloadFile(info.filename)}
                          >
                            Download
                          </button>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </main>

      <footer className="footer mt-5">
        <p>&copy; {new Date().getFullYear()} Instrumentalizer - Separate Vocals from Instrumentals</p>
      </footer>
    </div>
  );
}

export default App; 