const express = require("express")
const app = express()
const port = 8000;

const {faker} = require('@faker-js/faker')

// we can create a function to return a random / fake "product"
const createProduct = () => {
    const newFake = {
        name: faker.commerce.productName(),
        price: "$" + faker.commerce.price(),
        department: faker.commerce.department()
    }
    return newFake;
}

const newFakeProduct = createProduct();
console.log(newFakeProduct);

const createUser = () => {
    const newUser = {
        _id : faker.datatype.number(),
        firstName : faker.name.firstName(),
        lastName : faker.name.lastName(),
        email : faker.internet.email(),
        phoneNumber : faker.phone.number(),
        password : faker.internet.password()
    }
    return newUser
}

const createCompany = () => {
    const newCompany = {
        _id: faker.datatype.number(),
        name: faker.company.name(),
        address: {
            street: faker.address.streetAddress(),
            city: faker.address.city(),
            state: faker.address.state(),
            country: faker.address.country(),
            zipCode: faker.address.zipCode()
        }
    }
    return newCompany
}

const newFakeUser = createUser();
console.log(newFakeUser)
const newFakeCompany = createCompany();
console.log(newFakeCompany)

app.use(express.json());
app.use(express.urlencoded({ extended: true }))

// ROUTES AND LOGIC
app.get("/api/testing"), (req,res) => {
    res.json({ message: "Welcome to Faker API Assignment"})
}

// /api/users/new (get)
app.get("/api/users/new", (req, res) => {
    res.json(newFakeUser)
})
// /api/companies/new (get)
app.get("/api/companies/new", (req, res) => {
    res.json(newFakeCompany)
})
// /api/user/company (get)
app.get("/api/user/company", (req, res) => {
    res.json({newFakeUser, newFakeCompany})
})

//THIS STAYS AT THE BOTTOM
app.listen(port, () => console.log(`LISTENING ON PORT: ${port}`))


// const portVerb = faker.hacker.ingverb()
// app.listen(port, () => console.log(`${portVerb.charAt(0).toUpperCase() + portVerb.slice(1)} on port: ${port}`))

// const portVAN = faker.hacker.ingverb() + " " + faker.hacker.adjective() + " " + faker.hacker.noun()
// app.listen(port, () => console.log(`${portVAN.charAt(0).toUpperCase() + portVAN.slice(1)} on port: ${port}`))



// class User {
//     constructor() {
//         this.id = faker.datatype.number()
//         this.firstName = faker.name.firstName()
//         this.lastName = faker.name.lastName()
//         this.email = faker.internet.email()
//         this.phoneNumber = faker.phone.number()
//         this.password = faker.internet.password()
//     }
// }

// class Company {
//     constructor () {
//         this.id = faker.datatype.uuid()
//         this.name = faker.company.name()
//         this.address = [ {
//             Street: faker.address.street(),
//             City: faker.address.city(),
//             State: faker.address.state(),
//             Country: faker.address.country(),
//             Zipcode: faker.address.zipCode()
//         }]
//     }
// }

// // /api/users (post)
// app.post("/api/users", (req, res) => {
//     const newUser = new User()
//     res.json (newUser)
// })
// // /api/company (post)
// app.post("/api/company", (req, res) => {
//     const newCompany = new Company() // testing how it works within the route
//     res.json (newCompany)
// })