
document.getElementById('contatoForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const mensagem = document.getElementById('mensagem').value;
    if (nome && email && mensagem) {
        document.getElementById('formMsg').textContent = "Mensagem enviada com sucesso!";
    } else {
        document.getElementById('formMsg').textContent = "Por favor, preencha todos os campos.";
    }
});
