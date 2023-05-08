const mongoose = require("mongoose")

const JobSchema = new mongoose.Schema({
    title: {
        type: String,
        required: [true, "Title is required"],
        minLength: [3, "Title msut be 3 cahracters long"]
    },
    Company: {
        type: String,
        required: [true, "Company is required"],
        minLength: [3, "Company msut be 3 cahracters long"]
    },
    Salary: {
        type: Number,
        required: [true, "Salary is required"],
        min: [70000, "Salary must be at least 70000"]
    },
    isRemote: {
        type: Boolean,
        default: false
    },
    isApplied: {
        type: Boolean,
        default: false
    }
}, {timestamps: true})

// option 1
// option 2

module.exports.Job = mongoose.model('Job', JobSchema)