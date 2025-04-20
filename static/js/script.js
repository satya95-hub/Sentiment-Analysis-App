function openApp() {
    document.getElementById('curtain').classList.add('hidden');
    document.body.style.overflow = 'auto';
}

// Cleaned window.onload
window.onload = function () {
    const form = document.querySelector('form');
    const textarea = document.querySelector('textarea');
    const errorMessage = document.getElementById('error-message');
    const resultBox = document.querySelector('.result');

    if (form) {
        form.addEventListener('submit', function (e) {
            const inputText = textarea.value.trim();
            if (!inputText) {
                e.preventDefault(); // Stop form submission
                errorMessage.style.display = 'block';
                if (resultBox) {
                    resultBox.classList.add('hidden');
                }
            } else {
                errorMessage.style.display = 'none';
                if (resultBox) {
                    resultBox.classList.remove('hidden');
                }
            }
        });
    }
};
