# Meme Flask Website

**Made by Abhishek**

A simple Flask web application that displays random memes fetched from the Meme API. The page automatically refreshes every 10 seconds to show a new meme.

## Features

- Fetches random memes from [Meme API](https://meme-api.com/).
- Displays the meme image and the subreddit source.
- Auto-refreshes every 10 seconds.
- Manual refresh button.
- Responsive design using Bootstrap 5.

## Prerequisites

- Python 3.x installed on your system.
- `pip` (Python package installer).

## Installation & Setup

1.  **Clone or Download the project** to your local machine.

2.  **Navigate to the project directory**:
    Open your terminal or command prompt and change directory to the project folder:
    ```bash
    cd "meme app"
    ```

3.  **Set up a Virtual Environment** (Recommended):
    It's good practice to use a virtual environment to manage dependencies.
    
    *Windows:*
    ```bash
    python -m venv flask-venv
    flask-venv\Scripts\activate
    ```
    
    *macOS/Linux:*
    ```bash
    python3 -m venv flask-venv
    source flask-venv/bin/activate
    ```

4.  **Install Dependencies**:
    Install the required Python packages using `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

1.  Ensure your virtual environment is activated.

2.  Start the Flask server:
    ```bash
    python app.py
    ```
    
    **For development with debug mode enabled:**
    ```bash
    FLASK_DEBUG=true python app.py
    ```
    
    > **Note**: Debug mode is disabled by default for security. Only enable it during local development.

3.  You should see output indicating the server is running, typically:
    ```
    * Running on http://127.0.0.1:5000
    ```

4.  Open your web browser and visit:
    [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Project Structure

- `app.py`: The main Flask application file. It handles fetching the meme data and serving the webpage.
- `templates/index.html`: The HTML template that displays the meme. It includes the auto-refresh logic and styling.
- `test_app.py`: Unit tests for the Flask application.

## Continuous Integration (CI/CD)

This project includes a GitHub Actions workflow that automatically runs on every push and pull request to the `main` branch. The workflow performs the following checks:

### What the CI Workflow Does

1. **Sets up Python 3.10**: Configures a Python 3.10 environment for testing.

2. **Installs Dependencies**: 
   - Upgrades pip
   - Installs `flake8` for linting
   - Installs `pytest` for testing
   - Installs project dependencies from `requirements.txt`

3. **Linting with flake8**:
   - **Strict Check**: Stops the build if there are Python syntax errors or undefined names (using `E9,F63,F7,F82` rules)
   - **Warning Check**: Reports code style issues and complexity warnings (max line length: 127 characters, max complexity: 10)

4. **Testing with pytest**: Runs all unit tests to ensure the application works correctly.

### Running CI Checks Locally

To run the same checks locally before pushing:

```bash
# Install development dependencies
pip install flake8 pytest

# Run linting
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

# Run tests
pytest -v
```

The CI workflow helps maintain code quality and ensures that all changes are tested before being merged into the main branch.
