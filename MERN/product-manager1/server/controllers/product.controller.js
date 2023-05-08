const Product = require("../models/product.model")

// findAll, findOne, createOne, updateOne, deleteOne
// get, get, post, put, delete
// increase your error catch validations and .then logic
// result =/= response, write it out
// (result) => res.json({product: result}) - same as
    // findJoke => res.json(findJoke) etc. etc.

// api testing

// get
module.exports.findAll = (req, res) => {
    Product.find() //change res.json to result and not product:result
        .then((result) => res.json(result)) //left this as a result regularly in order to make FormPage apply.map function correctly
        .catch((err) => res.json({ message: "findAll function error", error: err }));
};

// get
module.exports.findOne = (req, res) => {
    Product.findOne({ _id: req.params.id }) // passing in result regularly here means I'd have to change the way ProductPage displays the details. No need for that atm
        .then((result) => res.json({ product: result }))
        .catch((err) => res.json({ message: "findOne error", error: err }));
};

// post
module.exports.createOne = (req, res) => {
    Product.create(req.body)
        .then((result) => res.json({ product: result })) 
        .catch((err) => res.json({ message: "createOne error", error: err }));
};

// put
module.exports.updateOne = (req, res) => {
    Product.updateOne(
        { _id: req.params.id },
        req.body,
        {new: true, runValidators: true}
        )
        .then((result) => res.json({ product: result }))
        .catch((err) => res.json({ message: "updateOne error", error: err }));
};

// delete
module.exports.deleteOne = (req, res) => {
    Product.deleteOne({ _id: req.params.id })
        .then(() => res.json({ message: `Deleted product with id: ${req.params.id}`}))
        .catch((err) => res.json({ message: "deleteOne error", error: err }));
};