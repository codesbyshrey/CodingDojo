const JokesAPI = require("../models/jokes.models")

module.exports.apiTest = (req, res) => {
    res.json({message: "Yay we're working"})
}

// approximate structure of module.exports
// module.exports.name = (req, res) => {
//     JokesAPI.function() //parenthesis not always required within .then and .catch thanks to single line arrow notation
//         .then((result) => res.json({ joke : result }))
//         .catch((err) => res.json(err)) //alternatively res.json ({message:"whoops", error:err})
// }

// all jokes
module.exports.allJokes = (req, res) => {
    JokesAPI.find()
        .then(jokeList => res.json(jokeList))
        .catch(err=>res.json(err))
}

// one joke
// id comes with underscores
module.exports.oneJoke = (req, res) => {
    JokesAPI.findOne({_id: req.params.id})
        .then(oneJoke => res.json(oneJoke))
        .catch(err=>res.json(err))}

// create joke
module.exports.createJoke = (req, res) => {
    // need to create a joke
    const newJoke = req.body
    JokesAPI.create(newJoke)
        .then(addedJoke => res.json(addedJoke))
        .catch(err=>res.json(err))}

// update joke (remember it's findOneAndUpdate not just update)
module.exports.updateJoke = (req, res) => {
    JokesAPI.findOneAndUpdate(
        {_id: req.params.id},
        req.body,
        {new:true, runValidators: true} //runvalidators not necessary, but helful
    )
        .then(updatedJoke => res.json(updatedJoke))
        .catch(err=>res.json(err))}

// delete joke
module.exports.deleteJoke = (req, res) => {
    JokesAPI.deleteOne({_id: req.params.id})
        .then(jokeList => res.json(jokeList))
        .catch(err=>res.json(err))}

// alternative method is to const everything like a function, and then module.exports everything in curlies