// 1. import all dependencies - CORS, MONGOOSE, EXPRESS, DOTENV

const express = require("express") // for some frameworks, somethings are in modules
const app = express()
const port = 8000 // just makes it easier for us to reference port as 8000 easier

require("dotenv").config();
const cors = require("cors")

require("./config/mongoose.config")

// 2. configure express
// make sure these lines are above any app.get or app.post code blocks
app.use(cors())
app.use( express.json() ); // recognize JSON object
app.use( express.urlencoded({ extended: true }) ); //to recognize the incoming Req object as strings/arrays

// make sure to include (app), and RENAME file ROUTE accordingly
require("./routes/PROJECTNAMESINGULAR.routes")(app)

// 3. Listen on the port
app.listen(port, ()=> console.log(`LISTENING AT PORT: ${port}`));

// comment out or cors and the required routes
// test with the api testing first to ensure the back end has worked
// get, create, update, delete
// get, put, post, delete

// CHECK WITH POSTMAN TO MAKE SURE ITS WORKING CORRECTLY, THATS HOW YOU CAN
// MOVE ON TO THE FRONT END, THAT WAY ALL THE BACKEND IS BASICALLY JUST TAKEN CARE OF

// const NameSchema = new mongoose.Schema ({}, {timestamps: true})
// module.exports.NAME = mongoose.model('name', NameSchema)
// ALTERNATIVE METHOD
// const Product = mongoose.model("Product", ProductSchema);
// module.exports = Product;