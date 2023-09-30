const openPopupButton = document.getElementById("open-popup");
const popupContainer = document.getElementById("popup-container");
const translateButton = document.getElementById("translate-button");

// Add an event listener to the popup container to handle language button clicks
popupContainer.addEventListener("click", (event) => {
    if (event.target.tagName === "BUTTON") {
        const selectedLanguage = event.target.textContent;

        // Hide the popup container
        popupContainer.style.display = "none";
    }
});

openPopupButton.addEventListener("click", () => {
    // const selectedLanguageElement = document.getElementById("selected-language");
    // selectedLanguageElement.textContent = "English";

    popupContainer.style.display = "flex";
});

translateButton.addEventListener("click", () => {
    // Hide the popup container before translating
    popupContainer.style.display = "none";

    translatePage();
});

function translatePage() {
    const targetLanguage = document.getElementById('targetLanguage').value;
    const contentToTranslate = document.body.innerHTML;

    // Send a request to the Translation API to translate the content
    fetch(`https://translation.googleapis.com/language/translate/v2?key=AIzaSyBn8mHJUP1N38npOK2Yd4pIE0Pg2y21sU0`, {
        method: 'POST',
        body: JSON.stringify({
            q: contentToTranslate,
            target: targetLanguage,
        }),
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        const translatedText = data.data.translations[0].translatedText;

        // Update the content of the current page with the translated content
        document.body.innerHTML = translatedText;
    })
    .catch(error => {
        console.error('Translation error:', error);
    });
}
