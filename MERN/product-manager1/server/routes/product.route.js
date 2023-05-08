const ProductController = require("../controllers/product.controller")

module.exports = (app) => {
    app.get("/api/products", ProductController.findAll)
    app.get("/api/products/:id", ProductController.findOne)
    // get posts have to be in order or we'll have some confusions
    app.put("/api/products/:id", ProductController.updateOne)
    app.post("/api/products", ProductController.createOne)
    app.delete("/api/products/:id", ProductController.deleteOne)
};

// find, update, create, delete
// get, put, post, delete