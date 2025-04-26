from flask import Flask, request, jsonify, send_from_directory
from speech_generator import generate_speech, start_ollama, stop_ollama
import os

app = Flask(__name__, static_folder=".")

@app.route("/")
def serve_html():
    # Serve the speech_vocalizer.html file
    return send_from_directory(".", "speech_vocalizer.html")

@app.route("/generate_speech", methods=["POST"])
def generate_speech_endpoint():
    data = request.get_json()
    topic = data.get("topic")
    if not topic:
        return "Topic is required.", 400

    start_ollama()  # Start Ollama before generating speech
    try:
        speech_text = generate_speech(topic)
        if speech_text:
            return jsonify({"speech_text": speech_text}), 200  # Ensure JSON response for consistency
        else:
            return "Failed to generate speech.", 500
    finally:
        stop_ollama()  # Stop Ollama after the task is completed

if __name__ == "__main__":
    app.run(debug=True, port=8000)  # Ensure the server runs on port 8000
