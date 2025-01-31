const fs = require('fs');
const express = require('express');
const app = express();

app.get('/', (req, res) => {
    // Read the count from the file
    let countText;
    try {
        countText = fs.readFileSync('./count.txt', 'utf-8');
    } catch (error) {
        // If the file doesn't exist or can't be read, default to 0
        countText = '0';
    }

    const count = parseInt(countText);
    console.log('Current count:', count);

    const newCount = count + 1;

    // Convert newCount to a string before writing
    fs.writeFileSync('./count.txt', String(newCount));

    res.send(`
        <!DOCTYPE html>
        <html lang="hu">
        <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            <title>Weboldal</title>
        </head>
        <body>
            <h1>Köszöntelek a weboldalamon</h1>
            <p> Ez az oldal ${newCount}-szor lett meglátogatva. </p>
        </body>
        </html>
    `);
});

app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});
