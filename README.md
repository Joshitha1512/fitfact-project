# fitfact-project
FitFact – Intelligent Fitness Claim Verifier

## FitFact Backend Setup

### API Endpoint
POST https://fitfact-backend.onrender.com/verify_claim

### Example Request
{
  "claim": "100 sit-ups burn belly fat"
}

### Example Response
{
  "verdict": "False",
  "explanation": "Spot reduction is a myth...",
  "sources": [...],
  "confidence": 0.95
}

