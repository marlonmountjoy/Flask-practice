# Flask Form Submission Application

## Overview
This project demonstrates a simple Flask web application that includes form submission and dynamic rendering of HTML pages. 
The application takes user input through a form, processes it, and displays the result on another page.

## Features
- A homepage with a form for user input.
- Handles form submissions and displays the submitted data on a result page.
- Simple HTML templates and Flask routes for dynamic functionality.

## File Structure
```
project-directory/
├── app.py                     # Main Flask application file
├── README.md                  # Documentation file
├── templates/                 # Directory for HTML templates
│   ├── index.html             # Static HTML page
│   └── result.html            # Result page for form submission
├── static/                    # Directory for static assets (optional)
│   └── style.css              # Example CSS file
├── .venv/                     # Virtual environment directory (ignored in Git)
└── requirements.txt           # List of Python dependencies
```

## Setup

### Prerequisites
- Python 3.8 or later installed on your system.
- `pip` (Python package manager).
- A virtual environment set up for the project.

### Steps to Run the Application

1. **Clone the Repository:**
   ```bash
   git clone (https://github.com/marlonmountjoy/Flask-practice.git)
   cd Flask-practice
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On macOS/Linux
   .venv\Scripts\activate    # On Windows
   ```

3. **Install Dependencies:**
   ```bash
   pip install flask
   ```

4. **Run the Application:**
   ```bash
   python app.py
   ```

5. **Access the Application:**
   - Open your browser and navigate to `http://127.0.0.1:5000/`.

## Usage
1. **Homepage:**
   - Displays a form where users can enter their name.
   - Form submission sends data to the server.

2. **Result Page:**
   - Displays the submitted name dynamically.

## Known Issues
- None currently.

## Contribution
- Feel free to fork this repository and make improvements.
- Submit a pull request with your changes.

## License
This project is licensed under the MIT License.

## Author
Marlon Mountjoy


