// 1. import all dependencies
const express = require("express") // for some frameworks, somethings are in modules
const app = express()
const port = 8000 // just makes it easier for us to reference port as 8000 easier

require("dotenv").config();
const cors = require("cors")

require("./config/mongoose.config")

// 2. configure express
// make sure these lines are above any app.get or app.post code blocks
app.use(cors())
app.use( express.json() ); // recognize JSON object
app.use( express.urlencoded({ extended: true }) ); //to recognize the incoming Req object as strings/arrays

require("./routes/job.routes")(app)

// 4. Listen on the port
app.listen(port, ()=> console.log(`Listening on port: ${port}`));