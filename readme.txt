# Flask Application

This is a Flask-based web application that processes and analyzes blood glucose data. Follow the steps below to set up and run the application.

## Prerequisites
Ensure you have the following installed on your system:
- Python (>=3.7)
- pip (Python package manager)

## Installation

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Create a Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Ensure all CSV files (`gl_df.csv`, `exercise_data.csv`, `food_intake.csv`, `medication_data.csv`) are in the root directory.

2. Run the Flask application:
   ```bash
   python app.py
   ```

3. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## API Endpoints
- `/` - Home page
- `/analyze` - Accepts JSON input with `user_id` and `date`, returns blood glucose analysis.
- Other static pages include `/about`, `/team`, `/services`, and more.

## Troubleshooting
- Ensure all required CSV files exist and have the correct columns.
- If dependencies fail, try updating pip:
  ```bash
  pip install --upgrade pip
  ```
- Use `export FLASK_APP=app.py` (Mac/Linux) or `set FLASK_APP=app.py` (Windows) if needed.

## License
This project is for educational purposes.

---

Happy Coding! 🚀

