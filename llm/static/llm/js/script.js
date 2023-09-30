const openPopupButton = document.getElementById("open-popup");
const popupContainer = document.getElementById("popup-container");
const languageOptions = document.getElementById("languageOptions");

let targetLanguage = "en";

languageOptions.addEventListener("click", (event) => {
    if (event.target.tagName === "BUTTON") {
        targetLanguage = event.target.value;
    }
});

openPopupButton.addEventListener("click", () => {
    popupContainer.style.display = "flex";
});

function translatePage() {
    const contentToTranslate = document.body.innerHTML;

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
        document.body.innerHTML = translatedText;
    })
    .catch(error => {
        console.error('Translation error:', error);
    });
}

// Event listener for the translate button
document.getElementById("translate-button").addEventListener("click", () => {
    popupContainer.style.display = "none";
    translatePage();
});









navigator.mediaDevices.getUserMedia({ audio: true })
  .then(function(stream) {
    const mediaRecorder = new MediaRecorder(stream);
    const chunks = [];

    mediaRecorder.ondataavailable = function(event) {
      if (event.data.size > 0) {
        chunks.push(event.data);
      }
    };

    document.getElementById('startRecording').addEventListener('click', function() {
      mediaRecorder.start();
      document.getElementById('startRecording').disabled = true;
      document.getElementById('stopRecording').disabled = false;
    });

    document.getElementById('stopRecording').addEventListener('click', function() {
      mediaRecorder.stop();
      document.getElementById('startRecording').disabled = false;
      document.getElementById('stopRecording').disabled = true;
    });

    mediaRecorder.onstop = function() {
      const audioBlob = new Blob(chunks, { type: 'audio/wav' });
      const audioUrl = URL.createObjectURL(audioBlob);
      document.getElementById('audioPlayer').src = audioUrl;
    };
  })
  .catch(function(error) {
    console.error('Error accessing the microphone:', error);
  });
