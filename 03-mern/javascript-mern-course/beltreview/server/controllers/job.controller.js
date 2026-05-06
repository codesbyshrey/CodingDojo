const { Job } = require("../models/job.model")

module.exports.apiTest = (req, res) => {
    res.json("Api Testing has worked")
}

// get all
module.exports.getAll = (req, res) => {
    //res.json("Get All has worked")
    Job.find()
        .then(allJobs => res.json(allJobs))
        .catch(err => res.status(400).json(err)) // consider error message?
}

// get one
module.exports.getOne = (req, res) => {
    Job.findOne( {_id : req.params.id} )
        .then(oneJob => res.json(oneJob))
        .catch(err => res.status(400).json(err))
}

// create
module.exports.addJob = (req, res) => {
    //res.json("Add Job has worked")
    Job.create(req.body)
        .then(newJob => res.json(newJob))
        .catch(err => res.status(400).json(err))
}

// update
module.exports.updateJob = (req, res) => {
    //res.json("Update Job has worked")
    Job.findOneAndUpdate(
        {_id:req.params.id},
        req.body,
        {new: true, runValidators: true} //validations inside update, not required
    )
        .then(updatedJob => res.json(updatedJob))
        .catch(err => res.status(400).json(err))
}

// delete
module.exports.deleteJob = (req, res) => {
    //res.json("Delete Job has worked")
    Job.deleteOne({_id: req.params.id})
        .then(message => res.json(message))
        .catch(err => res.status(400).json(err))
}

// get, create, update, delete
// get, put, post, delete

// CHECK WITH POSTMAN TO MAKE SURE ITS WORKING CORRECTLY, THATS HOW YOU CAN
// MOVE ON TO THE FRONT END, THAT WAY ALL THE BACKEND IS BASICALLY JUST TAKEN CARE OF