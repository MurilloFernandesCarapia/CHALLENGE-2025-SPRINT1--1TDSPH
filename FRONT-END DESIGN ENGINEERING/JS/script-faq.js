document.querySelectorAll('.faq-question').forEach(question => {
    question.addEventListener('click', () => {
        const item = question.parentElement;

        
        document.querySelectorAll('.faq-item').forEach(i => {
            if (i !== item) i.classList.remove('open');
        });

       
        item.classList.toggle('open');
    });
});