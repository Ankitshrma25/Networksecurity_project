# Network Security ML Pipeline

A machine learning project for network security threat detection and analysis using FastAPI and MLflow.

## Features

- **ML Training Pipeline**: Automated data ingestion, preprocessing, and model training
- **Model Serving**: FastAPI-based REST API for real-time predictions
- **Experiment Tracking**: MLflow integration for tracking models and experiments
- **Data Management**: MongoDB integration for distributed data storage
- **Model Management**: Pickle-based model serialization and loading

## Tech Stack

- **Framework**: FastAPI
- **ML Libraries**: scikit-learn, pandas, numpy
- **Database**: MongoDB
- **Model Tracking**: MLflow
- **Server**: Uvicorn
- **Configuration**: Python-dotenv, PyYAML

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd NetworkSecurity
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your MongoDB connection string
   ```

## Usage

### Start the API Server

```bash
python app.py
```

The API will be available at `http://localhost:8000`

### Run Training Pipeline

```bash
python main.py
```

### API Endpoints

- `GET /` - Home page
- `POST /predict` - Make predictions on network traffic data
- Additional endpoints as defined in `app.py`

## Project Structure

```
NetworkSecurity/
├── app.py                      # FastAPI application
├── main.py                     # Training pipeline entry point
├── requirements.txt            # Python dependencies
├── networksecurity/
│   ├── pipeline/              # Training and prediction pipelines
│   ├── utils/                 # Utility functions
│   ├── exception/             # Custom exceptions
│   ├── logging/               # Logging configuration
│   └── constant/              # Configuration constants
├── final_model/               # Trained models
│   ├── model.pkl
│   └── preprocessor.pkl
└── templates/                 # Jinja2 HTML templates
```

## Configuration

Environment variables (in `.env`):
- `MONGO_DB_URL` - MongoDB connection string (required)

## Files Overview

- **app.py**: Main FastAPI application with endpoints and CORS middleware
- **main.py**: Entry point for training pipeline
- **networksecurity/**: Core package containing ML pipeline logic

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome. Please feel free to submit a Pull Request.

## Troubleshooting

- Ensure MongoDB is accessible at the URL specified in `.env`
- Check that all dependencies are properly installed: `pip install -r requirements.txt`
- Verify Python version compatibility (3.8+)

## Notes

- Models are stored in `final_model/` directory
- Predictions output saved to `prediction_output/`
- MLflow artifacts are tracked in `mlflow.db`
