"""
Create a Flask app using an app factory and runs it.

"""
import os
from app import create_app

app = create_app(os.getenv("FLASK_CONFIG") or "development")

if __name__ == "__main__":
    app.run()
