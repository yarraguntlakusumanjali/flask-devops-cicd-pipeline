from flask import Flask, jsonify, render_template
import os

def create_app():
    app = Flask(__name__)

    @app.get("/")
    def home():
        return render_template("index.html", app_name=os.getenv("APP_NAME", "DevOps Demo"))

    @app.get("/health")
    def health():
        return jsonify(status="healthy", service=os.getenv("APP_NAME", "DevOps Demo")), 200

    @app.get("/api/info")
    def info():
        return jsonify(application=os.getenv("APP_NAME", "DevOps Demo"),
                       environment=os.getenv("APP_ENV", "development"),
                       version=os.getenv("APP_VERSION", "1.0.0")), 200
    return app
