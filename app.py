from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

def verify_claim_logic(claim):
    if "sit-ups" in claim.lower() and "belly fat" in claim.lower():
        return {
            "verdict": "False",
            "explanation": "Spot reduction is a myth. Sit-ups strengthen abs but do not burn belly fat.",
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6769371/"],
            "confidence": 0.95
        }
    else:
        return {
            "verdict": "Unverified",
            "explanation": "No matching claim found in knowledge base.",
            "sources": [],
            "confidence": 0.50
        }

# Home route to replace 404
@app.route("/", methods=["GET"])
def home():
    return "<h2>FitFact Backend is Running</h2>", 200

# Claim verification route
@app.route("/verify_claim", methods=["POST"])
def verify_claim():
    data = request.get_json()
    claim = data.get("claim", "")
    result = verify_claim_logic(claim)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
