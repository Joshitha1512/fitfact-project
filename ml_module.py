# Dummy ML/API module for testing backend

def verify_claim(claim: str):
    """
    Placeholder function - later replaced by Member 1's ML/API integration.
    Currently, just returns a fixed response for testing.
    """
    if "sit-ups" in claim.lower():
        return {
            "verdict": "False",
            "explanation": "Spot reduction is a myth. Sit-ups strengthen abs but do not burn belly fat.",
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6769371/"],
            "confidence": 0.95
        }
    else:
        return {
            "verdict": "Unverified",
            "explanation": "This claim is not in the knowledge base. Needs further review.",
            "sources": [],
            "confidence": 0.50
        }
