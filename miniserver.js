/*
Mini Servidor Express: Crear un servidor Express básico que responda "Hello World" en la ruta principal.
*/
const { json } = require('body-parser')
const express = require('express')
const app = express()
const PORT = 3050

app.use(json())

//callback
const callback = (req, res) => {
    res.status(200).json('Hello World')
}

app.get('/', callback)

app.listen(PORT, () => {
    console.log(`Server run in port: ${PORT}`)
})