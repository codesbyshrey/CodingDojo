const mongoose = require("mongoose")

const AuthorSchema = new mongoose.Schema({
    name: {
        type: String,
        required: [true, "Name of Author is required"],
        minLength: [3, "Author Name must be at least 3 characters long"]
    }}, { timestamps: true }
)

const Author = mongoose.model("Author", AuthorSchema)
module.exports = Author