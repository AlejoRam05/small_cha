//Mini Servidor Express: Crear un servidor Express básico que responda "Hello World" en la ruta principal.

// Arreglo de ejemplo para practicar CRUD
let productos = [
    { id: 1, nombre: "Laptop", descripcion: "Laptop de 14 pulgadas", precio: 800 },
    { id: 2, nombre: "Teléfono", descripcion: "Teléfono móvil de última generación", precio: 500 },
    { id: 3, nombre: "Tablet", descripcion: "Tablet con pantalla de 10 pulgadas", precio: 300 },
    { id: 4, nombre: "Monitor", descripcion: "Monitor HD de 24 pulgadas", precio: 150 }
];

const express = require('express');
const app = express()


app.get('/productos', (req, res) => {
    res.json(productos)
})


app.post('/productos', (req, res) => {
    const producto = req.body

    if (!producto || !producto.nombre || !producto.descripcion || !producto.precio){
        res.status(404).json({ mensaje: "El nuevo producto no cumple los requerimientos" })
    }
    productos.push(producto, id = productos.length + 1)
    res.status(201).json({ mensaje: "Producto agregado", producto });
})

app.delete('/productos/:id', (req, res) => {
    const id = parseInt(req.params.id)
    const index = productos.findIndex(producto => producto.id === id)

    if (!index){
        res.status(404).json({ mensaje: "Producto no encontrado" })
    }else{
        productos.splice(index, 1)
        res.status(200).json({ mensaje: "Producto eliminado" });
    }
})