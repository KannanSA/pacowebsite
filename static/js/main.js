// Initialize AOS animations
AOS.init({
    duration: 1000
});

// Toggle navigation menu
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    hamburger.addEventListener('click', function() {
        navMenu.classList.toggle('active');
    });
});
