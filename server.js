const { readFileSync, writeFileSync } = require('fs');
const express = require('express');
const app = express();
const counter = document.getElementById("szamlalo");

app.get('/', (req, res, counter) => {
    // Read the count from the file
    let countText;
    try {
        countText = readFileSync('./count.txt', 'utf-8');
    } catch (error) {
        // If the file doesn't exist or can't be read, default to 0
        countText = '0';
    }

    const count = parseInt(countText);
    console.log('Current count:', count);
    counter.innerHtml = `$(newCount)`

    const newCount = count + 1;

    // Convert newCount to a string before writing
    writeFileSync('./count.txt', String(newCount));

    res.send(`
        <!DOCTYPE html>
        <html lang="hu">
        <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            <title>IktProjekt</title>
        </head>
        <body>
            <h1>Köszöntelek a weboldalamon</h1>
            <p>Ez az oldal ${newCount}-szor/ször lett meglátogatva</p>
        </body>
        </html>
    `);
});
