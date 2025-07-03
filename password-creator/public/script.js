document.addEventListener('DOMContentLoaded', () => {
    const passwordEl = document.getElementById('password');
    const generateBtn = document.getElementById('generate-btn');

    const words1 = ["Brindle", "Mello", "Crystilly", "Plumble", "Grivvly", "Kooma", "Puri", "Marandhu"];
    const words2 = ["Spark", "fyStone", "Mark", "Quest", "Peak", "PattiKuppan", "yaladaTone", "pochuMark"];
    const numbers = ["7", "3", "8", "5", "4", "298", "2", "2"];
    const symbols = ["$", "#", "!", "%", "^", "&*", "*", "*"];

    function generatePassword() {
        const rand1 = Math.floor(Math.random() * words1.length);
        const rand2 = Math.floor(Math.random() * words2.length);
        const rand3 = Math.floor(Math.random() * numbers.length);
        const rand4 = Math.floor(Math.random() * symbols.length);

        const password = words1[rand1] + words2[rand2] + numbers[rand3] + symbols[rand4];
        passwordEl.textContent = password;
    }

    generateBtn.addEventListener('click', generatePassword);

    // Generate a password on initial load
    generatePassword();
});
