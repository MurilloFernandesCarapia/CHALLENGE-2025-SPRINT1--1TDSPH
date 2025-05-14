document.querySelectorAll('.faq-question').forEach(question => {
    question.addEventListener('click', () => {
        const item = question.parentElement;

        // Fecha os outros
        document.querySelectorAll('.faq-item').forEach(i => {
            if (i !== item) i.classList.remove('open');
        });

        // Alterna o clicado
        item.classList.toggle('open');
    });
});