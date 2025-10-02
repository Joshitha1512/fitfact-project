from flask import Flask, jsonify, request

app = Flask(__name__)

# Root route
@app.route("/")
def home():
    return """
    <h1>FitFact Backend is Live</h1>
    <p>Status: OK</p>
    <p>Available endpoints:</p>
    <ul>
        <li><a href='/health'>/health</a> - Health check</li>
        <li><a href='/info'>/info</a> - Project info</li>
        <li>POST /verify_claim - Claim verification (expects JSON)</li>
    </ul>
    """

# Health check
@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "FitFact Backend",
        "uptime": "running"
    })

# Info route
@app.route("/info")
def info():
    return jsonify({
        "project": "FitFact – Intelligent Text Verifier",
        "version": "v1.0",
        "description": "Backend API for claim verification (prototype)."
    })

# Verify Claim (main API)
@app.route("/verify_claim", methods=["POST"])
def verify_claim():
    data = request.get_json()
    claim_text = data.get("claim", "")

    return jsonify({
        "claim": claim_text,
        "verification_result": "This is a placeholder. AI verification will be added soon."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
