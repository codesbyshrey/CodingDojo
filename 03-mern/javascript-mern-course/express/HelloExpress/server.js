const express = require("express");
const app = express();
// have the ability to create routes and send some data

// we can hard code some users like this, later on we will store in DB
const users = [
  { firstName: "Reimu", lastName: "Hakurei" },
  { firstName: "Marisa", lastName: "Kirisame" },
  { firstName: "Sanae", lastName: "Kochiya" },
  { firstName: "Sakuya", lastName: "Izayoi" },
  { firstName: "Momiji", lastName: "Inubashiri" }
];

application.get("/api/users", (req, res) => {
  res.json(users);
});

// make sure these lines are above any ap.get or app.post code blocks
// to access post data, we need to pull from request object w/ new setting
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
// express middleware functions - responsible for providing and parsing the request.body data

// here's how we get form data
app.post('/api/users', (req, res) => {
  // req.body will containt the form data from Postman or from React
  console.log(req.body);
  // we canpush it into the users array for now, later into a database
  users.push(req.body);
  // always need to respond with something as well
  res.json({ status: "ok" });
})

// if we want to get a user with a specific id, we can make the id a part of the url
// be sure to preface the id variable with a `:` colon
app.get("/api/users/:id", (req, res) => {
  // we can get this `id` variable from req.params
  console.log(req.params.id);
  // assuming this id is the index of the users array we could return one user this way
  res.json(users[req.params.id]);
});

app.put("/api/users/:id", (req, res) => {
  // we can get this `id` variable from req.params
  const id = req.params.id;
  // assuming this id is the index of the users array we can replace the user like so
  users[id] = req.body;
  // we always need to respond with something
  res.json({ status: "ok" });
});

app.delete("/api/users/:id", (req, res) => {
  // we can get this `id` variable from req.params
  const id = req.params.id;
  // assuming this id is the index of the users array we can remove the user like so
  users.splice(id, 1);
  // we always need to respond with something
  res.json( { status: "ok" } );
});


//---------------------------------------------

// req is short for request
// res is short for response
app.get("/api", (req, res) => {
  // handle GET at route, second arg is callback function we want to run
  res.json({ message: "Hello World" });
  res.send("Our express api server is now sending this over to the browser");
});

// const port = 8000;
const server = app.listen(8000, () =>
  // actually runs our server on a specified port
  console.log(`Server is locked and loaded on port ${server.address().port}!`)
);

// this needs to be below the other code blocks
// app.listen (port, () => console.log('Listening on port: ${port}'));

// run by running server.js @ localhost:8000/api