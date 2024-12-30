const responseContainer = document.getElementById("response-container");
const addResponseButton = document.getElementById("add-response");
let responseIndex = 2;

addResponseButton.addEventListener("click", () => {
    if (responseIndex < 10) {
        responseIndex++;
        const input = document.createElement("input");
        input.type = "text";
        input.name = "poll_response"; // Important
        input.placeholder = `Réponse ${responseIndex}`;
        input.classList.add(
            "rounded-xl",
            "text-lg",
            "border-2",
            "border-gray-300",
            "focus:outline-none",
            "focus:ring-2",
            "focus:ring-blue-500",
            "focus:border-blue-500",
            "transition",
            "duration-200",
            "ease-in-out"
        );
        responseContainer.appendChild(input);
    }
});
