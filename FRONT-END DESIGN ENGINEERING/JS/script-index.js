
document.getElementById("openFormBtn").addEventListener("click", function () {
    document.getElementById("teleconsultaForm").classList.add("open");
    document.body.style.overflow = 'hidden'; 
});


function closeForm() {
    document.getElementById("teleconsultaForm").classList.remove("open");
    document.body.style.overflow = 'auto';
}


document.getElementById("consultaForm").addEventListener("submit", function (e) {
    e.preventDefault();
    alert("Voce entrou em uma reunião, aguarde o médico te atender!");
    closeForm();
});

function entrarNaTeleconsulta(event) {
    event.preventDefault(); 

    window.open("https://meet.google.com/abc-defg-hij", "_blank");
}
