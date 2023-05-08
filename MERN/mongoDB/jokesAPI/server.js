
const express = require("express") // for some frameworks, somethings are in modules

// import express from "express" (folder structure and setup changes things)
const app = express()
const port = 8000 // just makes it easier for us to reference port as 8000 easier

// require dotenv, config file, and jokes routes
require('dotenv').config()
require("./config/mongoose.config")

// routes have to be placed after the app.use
app.use(express.json())
app.use(express.urlencoded({extended:true}))

require("./routes/jokes.routes")(app)


// 00000 at the very end, below other code blocks 00000
app.listen(port, ()=> console.log(`LISTENING AT PORT: ${port}`));