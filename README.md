# Instrumentalizer

A web application that separates vocals from instrumentals in audio files using frequency filtering.

## Features

- Upload audio files in various formats (MP3, WAV, OGG, FLAC, AAC, M4A)
- Separate vocals from instrumentals using frequency-based filtering
- Progress tracking during processing
- Download separated tracks individually
- Clean, modern, and responsive UI
- Works with large audio files

## Project Structure

```
Instrumentalizer/
├── .gitignore
├── package.json
├── README.md
└── instrumentalizer/
    ├── backend/
    │   ├── app.py
    │   ├── requirements.txt
    │   ├── uploads/
    │   └── processed/
    └── frontend/
        ├── public/
        ├── src/
        └── package.json
```

## Setup and Installation

### Prerequisites

- Node.js (v14+)
- Python (v3.8+)
- npm or yarn

### Quick Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/instrumentalizer.git
   cd instrumentalizer
   ```

2. Install the dependencies for the root project:
   ```
   npm install
   ```

3. Install the frontend dependencies:
   ```
   npm run install:frontend
   ```

4. Set up the Python backend:
   ```
   cd instrumentalizer/backend
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   # OR
   source venv/bin/activate # macOS/Linux
   pip install -r requirements.txt
   ```

## Running the Application

After completing the setup, you can run the application using:

```
npm start
```

This will start both the backend server at http://localhost:5000 and the frontend at http://localhost:3000.

### Running Individual Components

To run just the frontend:
```
npm run start:frontend
```

To run just the backend:
```
npm run start:backend
```

## Usage

1. Open http://localhost:3000 in your web browser
2. Upload an audio file by dragging and dropping or clicking the upload area
3. Wait for the processing to complete (progress bar will indicate status)
4. Download the separated vocal and instrumental tracks

## How It Works

The application uses a frequency-based approach to separate vocals from instrumentals:

1. Audio is loaded and converted to the frequency domain using STFT
2. A frequency mask is applied to isolate frequencies typically associated with human voice
3. The mask is applied to create the vocal track, and inverted to create the instrumental track
4. Both tracks are saved and made available for download

This is a simplified approach and may not provide perfect separation, but works reasonably well for many audio files.

## License

MIT 