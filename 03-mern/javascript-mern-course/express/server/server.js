// npm init -y
// 1. import all dependencies
const express = require("express") // for some frameworks, somethings are in modules

// import express from "express" (folder structure and setup changes things)
const app = express()
const port = 8000 // just makes it easier for us to reference port as 8000 easier

// we can hard code some users like this
// later on we will want to store users in a database
const users = [
    { firstName: "Reimu",  lastName: "Hakurei"    },
    { firstName: "Marisa", lastName: "Kirisame"   },
    { firstName: "Sanae",  lastName: "Kochiya"    },
    { firstName: "Sakuya", lastName: "Izayoi"     },
    { firstName: "Momiji", lastName: "Inubashiri" }
];

// 2. Define Routes and Logic (GET, POST, PUT, PATCH, DELETE)
// first argument is the path you want to read (/api most times)
// req is short for request, goes first. res is for response
app.get("/api/testing", (req, res) => {
    // the route itself is the request / where it is happening
    // always need a corresponding response
    res.json({ message: "Hello World" });
});

app.get("/api/users", (req, res) => {
    res.json( users )
})

// 00000 at the very end, below other code blocks 00000
app.listen(port, ()=> console.log("Listening on port: 8000"));