// create MERN stack folder structure, front side is client, back side is server
const express = require("express")
const app = express();
const cors = require("cors");
const port = 8000

require("dotenv").config()
require("./config/mongoose.config")

// routes have to be placed after the app.use
app.use(express.json())
app.use(express.urlencoded({extended:true}))
app.use(cors()) // allows us to use cors for cross-origin full stack referencing

require("./routes/author.route")(app)


app.listen(port, () => console.log(`LISTENING AT PORT: ${port}`))