const translate = require('google-translate-api');

// Define the text you want to translate and the target language
const textToTranslate = 'Hello world';
const targetLanguage = 'es'; // Replace with the target language code

// Translate the text
translate(textToTranslate, { to: targetLanguage })
  .then((response) => {
    console.log(response.text);
  })
  .catch((error) => {
    console.error(error);
  });
