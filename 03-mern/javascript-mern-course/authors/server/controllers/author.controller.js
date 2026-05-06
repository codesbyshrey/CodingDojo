const Author = require("../models/author.model")

// findAll, findOne, createOne, updateOne, deleteOne
// get, get, post, put, delete
// increase your error catch validations and .then logic
// result =/= response, write it out
// (result) => res.json({product: result}) - same as
    // findJoke => res.json(findJoke) etc. etc.

// api testing

// get ({authors: result}) - how I'm used to interacting w/ data
// let's try and keep it closest to the belt review right now though
module.exports.findAll = (req, res) => {
    Author.find() //change res.json to result and not product:result
        .then((allAuthors) => res.json(allAuthors)) //left this as a result regularly in order to make FormPage apply.map function correctly
        .catch((err) => res.status(400).json({ message: "findAll function error", error: err }));
};

// get ({ author: result })
module.exports.findOne = (req, res) => {
    Author.findOne({ _id: req.params.id }) // passing in result regularly here means I'd have to change the way ProductPage displays the details. No need for that atm
        .then((oneAuthor) => res.json(oneAuthor))
        .catch((err) => res.status(400).json({ message: "findOne error", error: err }));
};

// post
module.exports.createOne = (req, res) => {
    Author.create(req.body)
        .then((createAuthor) => res.json(createAuthor)) 
        .catch((err) => res.status(400).json({ message: "createOne error", error: err }));
};

// put
module.exports.updateOne = (req, res) => {
    Author.findOneAndUpdate(
        { _id: req.params.id },
        req.body,
        {new: true, runValidators: true}
        )
        .then((updatedAuthor) => res.json(updatedAuthor))
        .catch((err) => res.status(400).json({ message: "findOneAndUpdate error", error: err }));
};

// delete
module.exports.deleteOne = (req, res) => {
    Author.deleteOne({ _id: req.params.id })
        .then(() => res.json({ message: `Deleted product with id: ${req.params.id}`}))
        .catch((err) => res.status(400).json({ message: "deleteOne error", error: err }));
};