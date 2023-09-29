const express = require('express');
const translate = require('@vitalets/google-translate-api');

const app = express();
const port = 3000;

app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.send(`
    <html>
    <head>
        <title>Translation Example</title>
    </head>
    <body>
        <select id="targetLanguage">
            <option value="en">English</option>
            <option value="hi">Hindi</option>
            <option value="mr">Marathi</option>
            <option value="pa">Punjabi</option>
            <option value="gu">Gujarati</option>
            <option value="ta">Tamil</option>
            <option value="te">Telugu</option>
            <!-- Add more Indian local languages as options -->
        </select>
        <button onclick="translatePage()">Translate</button>
        <div id="translatedContent"></div>

        <script>
            function translatePage() {
                const targetLanguage = document.getElementById('targetLanguage').value;
                const content = document.documentElement.innerHTML;
                
                // Send a request to the server for translation
                fetch('/translate', {
                    method: 'POST',
                    body: JSON.stringify({ content, targetLanguage }),
                    headers: {
                        'Content-Type': 'application/json',
                    },
                })
                .then(response => response.json())
                .then(data => {
                    document.getElementById('translatedContent').innerHTML = data.translatedContent;
                })
                .catch(error => {
                    console.error('Translation error:', error);
                });
            }
        </script>
    </body>
    </html>
  `);
});

app.post('/translate', async (req, res) => {
  const { content, targetLanguage } = req.body;

  try {
    // Translate the content using google-translate-api
    const translatedContent = await translate(content, { to: targetLanguage });
    res.json({ translatedContent: translatedContent.text });
  } catch (error) {
    console.error('Translation error:', error);
    res.status(500).send('Translation error');
  }
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
