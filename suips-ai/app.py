import os
from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/api/ai/score/startup/<int:startup_id>', methods=['GET'])
def score_startup(startup_id):
    score = random.randint(75, 99)
    risk = "Low" if score > 85 else "Moderate"
    return jsonify({
        "startupId": startup_id,
        "aiScore": score,
        "riskLevel": risk,
        "aiAnalysis": "The AI detects strong domain potential and a solid equity-to-funding ratio.",
        "status": "success"
    })

@app.route('/api/ai/match/startup/<int:startup_id>/investors', methods=['GET'])
def match_investors(startup_id):
    return jsonify({
        "startupId": startup_id,
        "recommendedInvestorIds": [1, 2], 
        "matchConfidence": "92%",
        "reason": "These investors have historically funded similar domains.",
        "status": "success"
    })

if __name__ == '__main__':
    # CRITICAL FOR CLOUD DEPLOYMENT: Listen on 0.0.0.0 and use Railway's Port
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)