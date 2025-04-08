# Project Setup Instructions

Follow the steps below to set up and run the project locally.

---

## Prerequisites

- Ensure you have Python installed on your system.
- Install `uv` from [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv).

---

## Installation and Setup

1. **Install Dependencies**
   
   In the project root directory, run the following command to install all dependencies using `uv`:
   ```bash
   uv sync
2. **Activate Vritual Environment**
    
    In the project root directory, run the following command to activate virtualenv which was created by README.md

    ```bash
    .venv\bin\activate or source .venv/bin/activate
3. **Run django application**
    ```bash
    python manage.py createmigrations
    python manage.py makemigrations
    python manage.py runserver
4. **Access Frontend**
    
    Since frontend is a simple html file , it can be accessed directly.
    just open signin.html and travel_request.html in browser. All communication happens through fetch api with CORS enabled locally.