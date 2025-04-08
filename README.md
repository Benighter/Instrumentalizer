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

## Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/Benighter/Instrumentalizer.git
   cd Instrumentalizer
   ```

2. **Install Dependencies**
   ```bash
   # Install root level dependencies
   npm install

   # Install frontend dependencies
   npm run install:frontend

   # Set up Python virtual environment and install backend dependencies
   cd instrumentalizer/backend
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate
   pip install -r requirements.txt
   cd ../..
   ```

3. **Start the Application**
   ```bash
   # Start both frontend and backend servers
   npm start
   ```

   The application will be available at:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:5000

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