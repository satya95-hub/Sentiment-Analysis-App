function openApp() {
    document.getElementById('curtain').classList.add('hidden');
    document.body.style.overflow = 'auto';
    sessionStorage.setItem('curtainHidden', 'true');
}

window.onload = function () {
    const curtain = document.getElementById('curtain');
    if (sessionStorage.getItem('curtainHidden') === 'true') {
        curtain.classList.add('hidden');
        document.body.style.overflow = 'auto';
    }

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
                sessionStorage.setItem('curtainHidden', 'true');
                errorMessage.style.display = 'none';
                if (resultBox) {
                    resultBox.classList.remove('hidden');
                }
            }
        });
    }
};
