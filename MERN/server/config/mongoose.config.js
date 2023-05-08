const mongoose = require('mongoose');

const dbName = "GENERAL SERVER NAME INSERT HERE"
const username = process.env.ATLAS_USERNAME // read variable in .env
const password = process.env.ATLAS_PASSWORD
const uri = `mongodb+srv://${username}:${password}@clusterdojo.debjcja.mongodb.net/${dbName}?retryWrites=true&w=majority`


mongoose.connect(uri, {useNewUrlParser: true, useUnifiedTopology: true})
    .then(() => console.log("Established a connection to the database"))
    .catch(err => console.log("Something went wrong when connecting to the database", err));    