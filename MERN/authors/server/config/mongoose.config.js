const mongoose = require('mongoose')
require("dotenv").config()

const dbName = "authorsdb"
const username = process.env.ATLAS_USERNAME
const password = process.env.ATLAS_PASSWORD

// needed from mongoDB ATLAS, make sure to click connect to files
const uri = `mongodb+srv://${username}:${password}@clusterdojo.debjcja.mongodb.net/${dbName}?retryWrites=true&w=majority`

mongoose.connect(uri, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
    })
    .then(() => console.log("Established a connection to our database"))
    .catch(err => console.log("Something went wrong when connecting to the database",err))