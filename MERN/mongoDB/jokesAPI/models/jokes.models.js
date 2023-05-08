const mongoose = require('mongoose')

// create our schema
const JokeSchema = new mongoose.Schema({
    setup: {
        type: String,
        required: [true, "Jokes Are Requires"],
        minLength: [10, "Jokes have to be 10 char long"]
    },
    punchline: {
        type: String,
        required: [true, "Punchlines are Required for HAHA"],
        minLength: [3, "Punchline must be 3 char long minimum"]
    }
}, {timestamps: true})
// don't forget to pass in the second argument w/ timestamps

// create JokesAPI
const JokesAPI = mongoose.model('joke', JokeSchema)
module.export = JokesAPI