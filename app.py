from flask import Flask, render_template, request, jsonify, session
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'phishing_awareness_game_secret_key_2024'

# Game data
QUIZ_QUESTIONS = [
    {
        "id": 1,
        "category": "Email Recognition",
        "question": "Which of these is a common phishing indicator in emails?",
        "options": [
            "Urgent action required with threats",
            "Professional formatting and branding",
            "Clear sender information",
            "Links to official websites"
        ],
        "correct": 0,
        "explanation": "Phishing emails often create urgency and use threats to pressure victims into taking immediate action without thinking critically."
    },
    {
        "id": 2,
        "category": "Email Recognition",
        "question": "What should you do if an email asks you to verify your password?",
        "options": [
            "Reply with your password immediately",
            "Click the link and update your password",
            "Never reply - legitimate companies don't ask for passwords via email",
            "Forward it to your friends"
        ],
        "correct": 2,
        "explanation": "Legitimate organizations never ask for passwords via email. This is a classic phishing tactic."
    },
    {
        "id": 3,
        "category": "Website Recognition",
        "question": "How can you verify a website is legitimate before entering sensitive information?",
        "options": [
            "Check if it has a nice design",
            "Look for HTTPS and a padlock icon in the address bar",
            "Check if it has lots of ads",
            "Ask a stranger online"
        ],
        "correct": 1,
        "explanation": "HTTPS (secure connection) and a padlock icon indicate the website uses encryption. Always check the URL carefully and look for these security indicators."
    },
    {
        "id": 4,
        "category": "Social Engineering",
        "question": "What is social engineering?",
        "options": [
            "Building social media profiles",
            "Manipulating people into divulging confidential information",
            "Creating social networks",
            "Organizing social events"
        ],
        "correct": 1,
        "explanation": "Social engineering is the art of manipulating people into revealing confidential information or performing actions that compromise security."
    },
    {
        "id": 5,
        "category": "Best Practices",
        "question": "What is the best practice for passwords?",
        "options": [
            "Use your birthday as password",
            "Use the same password for all accounts",
            "Use strong, unique passwords for each account",
            "Write passwords on sticky notes"
        ],
        "correct": 2,
        "explanation": "Strong, unique passwords for each account significantly reduce the risk of unauthorized access if one account is compromised."
    },
    {
        "id": 6,
        "category": "Email Recognition",
        "question": "A suspicious email claims to be from your bank. What's the safest action?",
        "options": [
            "Click the link in the email to verify",
            "Call your bank using the number on your bank card or official website",
            "Reply to the email asking for verification",
            "Ignore it and do nothing"
        ],
        "correct": 1,
        "explanation": "Always contact the organization directly using contact information from official sources, not from the suspicious email."
    },
    {
        "id": 7,
        "category": "Website Recognition",
        "question": "What's a red flag for a fake website?",
        "options": [
            "Professional logo and design",
            "Misspelled domain name or unusual URL",
            "Clear contact information",
            "Customer testimonials"
        ],
        "correct": 1,
        "explanation": "Fake websites often have slightly misspelled domain names (like 'amaz0n.com' instead of 'amazon.com') to trick users."
    },
    {
        "id": 8,
        "category": "Social Engineering",
        "question": "A caller claims to be from IT support and asks for your password. What do you do?",
        "options": [
            "Give them your password",
            "Hang up and call IT directly using official contact info",
            "Ask them to call back later",
            "Give them a fake password"
        ],
        "correct": 1,
        "explanation": "Legitimate IT support will never ask for your password. Always verify by calling the organization directly."
    }
]

EMAIL_EXAMPLES = [
    {
        "id": 1,
        "subject": "URGENT: Verify Your Account Now!",
        "from": "security@paypa1.com",
        "body": "Dear Customer,\n\nYour account has been compromised. Click here immediately to verify your identity and secure your account.\n\nClick: http://paypa1-verify.com/login",
        "red_flags": [
            "Urgent language with threats",
            "Misspelled domain (paypa1 instead of paypal)",
            "Suspicious link URL",
            "Generic greeting"
        ],
        "is_phishing": True
    },
    {
        "id": 2,
        "subject": "Your Amazon Order Confirmation",
        "from": "orders@amazon.com",
        "body": "Thank you for your order!\n\nOrder ID: AMZ-123456\nTotal: $49.99\n\nYou can track your package at: https://www.amazon.com/orders/123456",
        "red_flags": [],
        "is_phishing": False
    },
    {
        "id": 3,
        "subject": "Congratulations! You've Won a Prize!",
        "from": "winner@lotteryprize.net",
        "body": "You have been selected as a winner! Claim your $1,000,000 prize by clicking the link below and providing your banking details.\n\nClaim Prize: http://lotteryprize-claim.net/winner",
        "red_flags": [
            "Too good to be true offer",
            "Requests banking information",
            "Suspicious domain",
            "Unsolicited prize notification"
        ],
        "is_phishing": True
    }
]

WEBSITE_EXAMPLES = [
    {
        "id": 1,
        "name": "Legitimate Bank Website",
        "url": "https://www.yourbank.com",
        "features": [
            "HTTPS with padlock icon",
            "Official domain name",
            "Professional design",
            "Clear security information"
        ],
        "is_phishing": False
    },
    {
        "id": 2,
        "name": "Fake Bank Website",
        "url": "http://www.yourbank-secure.net",
        "features": [
            "HTTP (not HTTPS)",
            "Slightly different domain",
            "Similar but slightly off design",
            "Requests password immediately"
        ],
        "is_phishing": True
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/api/quiz', methods=['GET'])
def get_quiz():
    """Get quiz questions"""
    return jsonify(QUIZ_QUESTIONS)

@app.route('/api/email-examples', methods=['GET'])
def get_email_examples():
    """Get email examples for analysis"""
    return jsonify(EMAIL_EXAMPLES)

@app.route('/api/website-examples', methods=['GET'])
def get_website_examples():
    """Get website examples for analysis"""
    return jsonify(WEBSITE_EXAMPLES)

@app.route('/api/submit-answer', methods=['POST'])
def submit_answer():
    """Submit quiz answer and get feedback"""
    data = request.json
    question_id = data.get('question_id')
    selected_answer = data.get('selected_answer')
    
    question = next((q for q in QUIZ_QUESTIONS if q['id'] == question_id), None)
    
    if not question:
        return jsonify({'error': 'Question not found'}), 404
    
    is_correct = selected_answer == question['correct']
    
    return jsonify({
        'is_correct': is_correct,
        'correct_answer': question['correct'],
        'explanation': question['explanation']
    })

@app.route('/api/analyze-email', methods=['POST'])
def analyze_email():
    """Analyze email for phishing indicators"""
    data = request.json
    email_id = data.get('email_id')
    user_answer = data.get('is_phishing')
    
    email = next((e for e in EMAIL_EXAMPLES if e['id'] == email_id), None)
    
    if not email:
        return jsonify({'error': 'Email not found'}), 404
    
    is_correct = user_answer == email['is_phishing']
    
    return jsonify({
        'is_correct': is_correct,
        'actual_answer': email['is_phishing'],
        'red_flags': email['red_flags'],
        'explanation': 'Phishing email' if email['is_phishing'] else 'Legitimate email'
    })

@app.route('/api/analyze-website', methods=['POST'])
def analyze_website():
    """Analyze website for phishing indicators"""
    data = request.json
    website_id = data.get('website_id')
    user_answer = data.get('is_phishing')
    
    website = next((w for w in WEBSITE_EXAMPLES if w['id'] == website_id), None)
    
    if not website:
        return jsonify({'error': 'Website not found'}), 404
    
    is_correct = user_answer == website['is_phishing']
    
    return jsonify({
        'is_correct': is_correct,
        'actual_answer': website['is_phishing'],
        'features': website['features'],
        'explanation': 'Phishing website' if website['is_phishing'] else 'Legitimate website'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)

