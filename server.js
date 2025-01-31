const { readFileSync, writeFileSync } = require('fs');
const express = require('express');
const app = express();
const counter = document.getElementById("szamlalo");
const count = parseInt(countText);
console.log("asd")

app.get('/', (req, res, counter) => {
    // Read the count from the file
    let countText;
    console.log("asdf")
    try {
        countText = readFileSync('./count.txt', 'utf-8');
        counter.innerText = count;
    } catch (error) {
        // If the file doesn't exist or can't be read, default to 0
        countText = '0';
    }
    console.log("asdfg")
    console.log('Current count:', count);
    counter.innerHtml = `$(newCount)`
    console.log("asdfgh")

    const newCount = count + 1;

    // Convert newCount to a string before writing
    writeFileSync('./count.txt', String(newCount));
    console.log("asdfghj")
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
