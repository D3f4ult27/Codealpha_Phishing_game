#  Phishing Awareness Game

An interactive educational web application designed to teach users about phishing attacks, social engineering tactics, and cybersecurity best practices.

## Features

✨ **Interactive Game Modes:**
- **Quiz Challenge**: Answer questions about phishing recognition, social engineering, and security best practices
- **Email Analysis**: Identify phishing emails by analyzing real-world examples
- **Website Analysis**: Spot fake websites and learn security indicators

📚 **Educational Content:**
- Real-world phishing email examples
- Fake website scenarios
- Red flags and warning signs
- Best practices and tips
- Instant feedback on answers

🎯 **Game Mechanics:**
- Session-based scoring (no database required)
- Multiple game modes to choose from
- Progress tracking
- Performance feedback
- Engaging UI with smooth animations

## Project Structure

```
.
├── app.py                 # Flask application and API endpoints
├── requirements.txt       # Python dependencies
├── templates/
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Home page
│   └── game.html         # Game interface
└── static/
    ├── style.css         # Styling
    └── script.js         # Client-side functionality
```

## Installation

1. **Clone or download the project**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open in browser:**
   Navigate to `http://localhost:5000/`

## How to Play

1. **Home Page**: Learn about phishing and why it's important
2. **Start Game**: Click "Play Game" or "Start Playing"
3. **Choose Mode**: Select from Quiz, Email Analysis, or Website Analysis
4. **Answer Questions**: Respond to each question/scenario
5. **Get Feedback**: Receive instant feedback with explanations
6. **View Results**: See your final score and performance

## Game Modes Explained

### Quiz Challenge
Answer 8 multiple-choice questions covering:
- Email recognition techniques
- Website security indicators
- Social engineering tactics
- Cybersecurity best practices

### Email Analysis
Analyze 3 real-world email examples and determine if they are phishing attempts. Learn to spot:
- Urgent language and threats
- Misspelled domains
- Suspicious links
- Generic greetings

### Website Analysis
Evaluate 2 website examples and identify phishing indicators such as:
- HTTP vs HTTPS
- Domain name variations
- Design inconsistencies
- Immediate password requests

## Scoring System

- **10 points** per correct answer
- **Maximum score**: Varies by game mode (80-100 points)
- **Accuracy percentage**: Calculated based on correct answers
- **Performance feedback**: Based on final score

## Educational Content

### Topics Covered

1. **Email Recognition**
   - Identifying phishing emails
   - Spotting red flags
   - Verifying sender information

2. **Website Security**
   - HTTPS and SSL certificates
   - Domain verification
   - Legitimate vs fake websites

3. **Social Engineering**
   - Manipulation tactics
   - Pretexting and phishing
   - Password security

4. **Best Practices**
   - Strong password creation
   - Two-factor authentication
   - Reporting suspicious activity

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript
- **No Database**: Session-based, no user data storage
- **Responsive Design**: Works on desktop and mobile devices

## API Endpoints

- `GET /` - Home page
- `GET /game` - Game interface
- `GET /api/quiz` - Get quiz questions
- `GET /api/email-examples` - Get email examples
- `GET /api/website-examples` - Get website examples
- `POST /api/submit-answer` - Submit quiz answer
- `POST /api/analyze-email` - Analyze email answer
- `POST /api/analyze-website` - Analyze website answer

## Browser Compatibility

- Chrome/Chromium
- Firefox
- Safari
- Edge
- Mobile browsers

## Notes

- No user data is stored or collected
- Session-based scoring only
- All data is processed client-side
- No external API calls required
- Fully self-contained application

## Future Enhancements

Potential features to add:
- More quiz questions and examples
- Difficulty levels
- Leaderboard (local storage)
- Certificate of completion
- Mobile app version
- Multi-language support
- Video tutorials
- Real-time phishing alerts

## License

Educational use only. Feel free to modify and distribute for educational purposes.

## Support

For issues or suggestions, please review the code and customize as needed for your educational environment.

---

**Stay Safe Online! 🔒**

