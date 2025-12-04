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

3.  You should see output indicating the server is running, typically:
    ```
    * Running on http://127.0.0.1:5000
    ```

4.  Open your web browser and visit:
    [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Project Structure

- `app.py`: The main Flask application file. It handles fetching the meme data and serving the webpage.
- `templates/index.html`: The HTML template that displays the meme. It includes the auto-refresh logic and styling.
