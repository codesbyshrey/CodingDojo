const express = require('express');
const cors = require('cors') // allows us to make cross origin requests
const app = express();
const port = 8000;

app.use(cors()) // allows us to use cors

require('./server/routes/person.routes')(app); // this is new for us
// now we should get a JSON response for hello world

// GOES AT THE BOTTOM
app.listen(port, () => console.log(`LISTENING AT PORT: ${port}`) );

// we will be running two different servers
// front end react server with live reloading and express server