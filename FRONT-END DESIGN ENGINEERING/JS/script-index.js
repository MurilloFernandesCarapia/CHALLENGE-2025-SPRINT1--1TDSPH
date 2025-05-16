
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
  alert("Sua consulta foi marcada! Agora aguarde uma mensagem chegar no seu Whatsapp!");
  closeForm();
});



window.watsonAssistantChatOptions = {
  integrationID: "0f3f87f3-1c24-4707-82b2-8fb67f3394c7", // The ID of this integration.
  region: "us-south", // The region your integration is hosted in.
  serviceInstanceID: "f4d2aa34-3d0f-453c-9455-bab624ab83ac", // The ID of your service instance.
  onLoad: async (instance) => { await instance.render(); }
};
setTimeout(function () {
  const t = document.createElement('script');
  t.src = "https://web-chat.global.assistant.watson.appdomain.cloud/versions/" + (window.watsonAssistantChatOptions.clientVersion || 'latest') + "/WatsonAssistantChatEntry.js";
  document.head.appendChild(t);
});

const formulario = document.getElementById("consultaForm");
console.log(formulario);

formulario.addEventListener("submit", function(e){

  e.preventDefault();
// recuperando os campos/input
  const nome = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const whatsapp = document.getElementById("whatsapp").value.trim();

  let usuario = {
    nomeObj : nome,
    emailObj : email,
    whatsappObj : whatsapp
  }

  try {
    
    if(usuario.nomeObj == "" || (usuario.nomeObj == undefined)){
      throw new Error("O campo deve ser preenchido com o nome!")
    }
    if(usuario.emailObj == "" || (usuario.emailObj == undefined)){
      throw new Error("O campo deve ser preenchido com o email!")
    }
    if(usuario.whatsappObj == "" || (usuario.whatsappObj == undefined)){
      throw new Error("O campo deve ser preenchido com o número do Whatsapp!")
    }



  } catch (error) {
    alert(error);
    
  }

  formulario.reset();

  

});



