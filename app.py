from flask import Flask, request, jsonify

app = Flask(__name__)

# Root route
@app.route("/", methods=["GET"])
def home():
    return """
        <h1>FitFact Backend is Running</h1>
        <p>Status: OK</p>
        <p>Use the <code>/verify_claim</code> endpoint to check fitness-related claims.</p>
    """, 200

# Health check route
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

# Main API route
@app.route("/verify_claim", methods=["POST"])
def verify_claim():
    data = request.get_json()
    claim = data.get("claim", "")
    
    # Placeholder response (later will be replaced with ML/NLP model)
    response = {
        "claim": claim,
        "verification_result": "This is a placeholder. AI verification will be added soon."
    }
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
