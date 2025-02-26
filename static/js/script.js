const hamburger = document.getElementById('hamburger');
const profileHamburger = document.getElementById('profile-hamburger');
const sidePanel = document.getElementById('sidePanel');

const profilePanel = document.getElementById('profilePanel');

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    sidePanel.classList.toggle('active');
});

profileHamburger.addEventListener('click', () => {
    profileHamburger.classList.toggle('active');
    profilePanel.classList.toggle('active');
});