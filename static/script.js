// Global script for the Phishing Awareness Game

// Smooth scroll behavior
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Add animation on page load
window.addEventListener('load', function() {
    const cards = document.querySelectorAll('.feature-card, .mode-btn');
    cards.forEach((card, index) => {
        card.style.animation = `fadeInUp 0.5s ease-out ${index * 0.1}s both`;
    });
});

// Fade in animation
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
`;
document.head.appendChild(style);

// Prevent accidental navigation
let gameInProgress = false;

function setGameInProgress(inProgress) {
    gameInProgress = inProgress;
}

window.addEventListener('beforeunload', function(e) {
    if (gameInProgress) {
        e.preventDefault();
        e.returnValue = '';
    }
});

