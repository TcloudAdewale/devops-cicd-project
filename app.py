from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from Tcloud's DevOps Pipeline! 🚀",
        "status": "running",
        "engineer": "Abidemi Adewale",
        "stack": ["Python", "Flask", "Docker", "GitHub Actions"]
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
