const mongoose = require("mongoose");

const ProductSchema = new mongoose.Schema ({
    title: {
        type: String,
        required: [true, "Title is required"],
        minLength: [3, "Title of Product must be at least 3 characters"],
    },
    price: {
        type: Number,
        required: [true, "Prices are required"],
        min: [1, "Price must be some value"],
    },
    description: {
        type: String,
        required: [true, "Descriptions of Products are required"],
        minLength: [3, "Descriptions must be at least 3 characers"],
    }
})

// create product and mongoose.model it, then export
const Product = mongoose.model("Product", ProductSchema);
module.exports = Product;