const JobController = require("../controllers/job.controller")

module.exports = (app) => {
    app.get("/api/testing", JobController.apiTest)
    app.get("/api/jobs", JobController.getAll)
    app.get("/api/jobs/:id", JobController.getOne)
    // the order of the gets follows sequentially
    app.post("/api/jobs", JobController.addJob)
    app.put("/api/jobs/:id", JobController.updateJob)
    app.delete("/api/jobs/:id", JobController.deleteJob)
}