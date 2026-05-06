# AJAX and APIs
 OBJECTIVES
  - Learn what APIs are in the context of web developmet

APIs define rules to interact with a particular application. Easy to access information in logical steps.

## Every API is Different

Every API behaves according to its developer, and some will often require authentication. Don't forget to hide API keys from public access, otherwise you can run the risk of losing your authentication privileges.

Servers will pass information via URL or forms, server returns JSON and other similar formats
 - JavaScript Object Notation
  --> basically a series of dictionaries arranged in particular indexing manner

## What's the Big Deal

 - SPEED
     - developers will have an easier time implementing and accessing information to build cool applications
 - CROSS DEVELOPMENT
     - managers and developers can speak to each other across the different languages.
     - Three teams with diff developers and languages
     --> either everyone migrates to one language (bad) or they build APIs so that they can work together in an integrated manner without having to learn to work together
 - WIDER REACH OF AUDIENCE
     - natural incresae in accessible audience, and builds brand quickly

# AJAX
OBJECTIVES
 - Learn what AJAX allows us to do
 - Understand its significance to the modern web
 - Synchronous vs Asynchronous

AJAX stands for
Asynchronous
Javascript
And
XML

## Synchronous vs Asynchronous

 - JavaScript --> example of synchronous by design, reads line-by-line one at a time. Sometimes we want multiple things happening at once.
 - Restaurant analogy with the servers and attending tables

AJAX is essentially a group of technology that allows a developer to change parts of a website with new content from servers without reloading the page.

JavaScript methods allow us to retrieve information in this manner.

# FETCHING DATA
OBJECTIVES
 - Understand what the Fetch method dous
 - How to use fetch with promises and async/wait

## HTTPS REQUEST-RESPONSE CYCLE

Sometimes we don't want our server requests to display a web page, sometimes we just want to access the data. We can utilize the RRC with a built-in Javascript method called FETCH

## FETCH METHOD

Makes a GET request to an API server --> 2 methods to implement

GithubAPI as example with PROMISES:
```js
fetch("https://api.github.com/users/adion81")
     .then(response => response.json())
     .then(coderData => console.log(coderData))
     .catch(err => console.log(err))
```

almost like a chain reaction
 - request via FETCH, THEN wait, THEN convert to JSON. CATCH helps us see the errors coming back

Arrow Syntax is Arrow Functions. More compact way of expressing a function

GithubAPI as example with ASYNC/AWAIT
```js
async function getCoderData() {
     // the await keyword lets js know that it needs to wait until it gets a response back to continue
     var response = await fetch("https://api.github.com/users/adion81");
     // we then need to convert the data into JSON format
     var coderData = await response.json();
     return coderData;
}

console.log(getCoderData());
```

Apply the async keyword to the function, and then await for the data to come back. Always returns the data after it comes back.

BOTH THE ABOVE EXAMPLES WILL GET BACK THE SAME RESULT. BOTH ARE USING ASYNCHRONOUS BEHAVIOR TO GET DATA BACK TO US, THE DEVELOPER.

# JSON
OBJECTIVES
 - Understand what JSON data is
 - Learn how to access the valuees stored inside a JSON object

## What is JSON

JavaScript Object Notation --> lightweight format to store and transport data, stored as key:value pairs.
 - this is the standard return type of most 
 - LEARN platform has better material, copy paste it later

Array.isArray(someVariable) can help you check if a variable is an array type object, since JS stores all parts of the data structure as object type

We can access values with dot or square bracket notation.

## Accessing JSON

console.log(data) where data is a var that an object is assigned to, would print out an image with indexed dictionaries.

# API KEYS
OBJECTIVES
 - understand how to use an API key to access API data

Help track information about API usage and help promote monetization of useful APIs.

```js
/*
http://api.openweathermap.org/data/2.5/forecast/daily?id=524901&APPID={INSERTAPIKEY}

// Make sure to put your unique api key in the URL and take out the brackets
// &APPID={INSERTAPIKEY} will need to be at the end of each URL that you access below and in the DojoWeather
*/
```

Every single request you send to an API will have to include that API key. Free tiers let you play around with some data pretty easily.