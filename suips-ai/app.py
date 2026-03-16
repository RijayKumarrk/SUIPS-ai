from flask import Flask, jsonify
import random

app = Flask(__name__)

# 1. AI Startup Scoring Endpoint
@app.route('/api/ai/score/<int:startup_id>', methods=['GET'])
def score_startup(startup_id):
    # Mocking an AI evaluation (In real life, fetch from DB & run ML model)
    score = random.randint(75, 99)
    risk = "Low" if score > 85 else "Moderate"
    
    return jsonify({
        "startupId": startup_id,
        "aiScore": score,
        "riskLevel": risk,
        "aiAnalysis": "The AI detects strong domain potential and a solid equity-to-funding ratio.",
        "status": "success"
    })

# 2. AI Investor Matchmaking Endpoint
@app.route('/api/ai/match/investors-for-startup/<int:startup_id>', methods=['GET'])
def match_investors(startup_id):
    # Mocking an AI recommendation engine
    return jsonify({
        "startupId": startup_id,
        "recommendedInvestorIds": [2, 4, 7], # Mock investor IDs from DB
        "matchConfidence": "92%",
        "reason": "These investors have historically funded AI and FinTech domains with similar budgets.",
        "status": "success"
    })

if __name__ == '__main__':
    # Run on port 5000 to match the Java RestTemplate configuration!
    app.run(port=5000, debug=True)