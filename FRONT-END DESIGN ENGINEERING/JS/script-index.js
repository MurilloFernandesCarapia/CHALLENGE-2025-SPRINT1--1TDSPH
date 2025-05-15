
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
  setTimeout(function(){
    const t=document.createElement('script');
    t.src="https://web-chat.global.assistant.watson.appdomain.cloud/versions/" + (window.watsonAssistantChatOptions.clientVersion || 'latest') + "/WatsonAssistantChatEntry.js";
    document.head.appendChild(t);
  });


