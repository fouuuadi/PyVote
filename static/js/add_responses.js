document.addEventListener("DOMContentLoaded", () => {
    const responseContainer = document.getElementById("response-container");
    const addResponseButton = document.getElementById("add-response");

    // Compteur initial basé sur les inputs existants
    let responseCount = responseContainer.querySelectorAll(".response-input").length;

    addResponseButton.addEventListener("click", () => {
        if (responseCount >= 10) {
            alert("Vous ne pouvez pas ajouter plus de 10 réponses.");
            return;
        }

        // Incrémenter le compteur et créer un nouvel input
        responseCount++;
        const newInput = document.createElement("input");
        newInput.type = "text";
        newInput.name = "poll_response[]";
        newInput.className = "response-input rounded-xl text-lg border-2 border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-200 ease-in-out";
        newInput.placeholder = `Réponse ${responseCount}`;
        newInput.required = true;

        // Ajouter l'input au conteneur
        responseContainer.appendChild(newInput);
    });
});
