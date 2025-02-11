from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask is running on Render!"

@app.route("/watch/<video_id>", methods=["GET"])
def watch_video(video_id):
    return jsonify({"message": f"Streaming video: {video_id}"})

if __name__ == "__main__":
    app.run(debug=True)
