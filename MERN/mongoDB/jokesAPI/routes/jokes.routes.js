const JokeController = require("../controllers/jokes.controller")

module.exports = (app) => {
    app.get("/api/testing", JokeController.apiTest)
    // make sure :id is in your route
    app.get("/api/jokes", JokeController.allJokes)
    app.get("/api/jokes/:id", JokeController.oneJoke)
    // order of the gets matters, cannot reorganize unless we change type of HTTP request
    app.post("/api/jokes", JokeController.createJoke)
    app.put("/api/jokes/:id", JokeController.updateJoke)
    app.delete("/api/jokes/:id", JokeController.deleteJoke)
}