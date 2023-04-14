# W1D5 FLASK: Session and POST
https://www.youtube.com/watch?v=4SMGPHKzdLQ&list=PLp3jkMF9o45ikcn7i_q_vOYNytJCuv8IB&index=22

 - By default, flask methods default to GET methods
 - we need to enable POST method, and then request that information back via print(request.form)
 - immutable multi-dictionary in terminal (TUPLE)
 print(request.form('first_name')) - will show your first name in the Terminal
      - it is looking for the name in that element to match with the key, not the id (HTML id is different from SQL id)
------------------------------
 - put your values inside the jinja tags on your HTML {}
 - {{request.form['first_name']}}
 - OR on FLASK side: first_name = request.form['first_name'] and then pass it into to the render template after html
 -----------------------------
 1. Display Route
 2. Action Route --> doing some kind of action on that information
 - be careful about resubmission of form (we don't want to render a page that is also processing information - double credit card charge)
 - Action routes shouldn't display templates (just let display routes do that) --> return REDIRECT ('/') --> to the app.route, not the template
      - REDIRECT doesn't take in our form information

It would be nice if there was a tool to use that could carry the name and values into any function we want. SESSION
 - What is Session? --> saves user info if they're logged in
 - Session is a DICTIONARY data type, meaning it takes in key value pairs
 - If they key doesn't exist, it'll add that key and value
 - If you try and edit it afterwards, you will overwrite
 - Server Client Relationship: session sends info to client in the form of a COOKIE
     - pulls back a cookie the next time we use cookie --> storing the users data on the client side
1. In Your Action Route:
     - session['user_details'] = {
          'first_name' : request.form['first_name']
          'last_name' : request.form['last_name']
          'age' : request.form['age']
     }
     - In order to use SESSION, we have to use a SECRET KEY (in our server.py)
     - attached to the instance as an attribute of secret_key
     - app.secret_key = "keep it secret, keep it safe"
 - Session Persists Everywhere
     - Allows us to just say session.user_details.first_name inside of our jinja tags on our HTML template
 - BETTER METHOD IN FLASK:
     - session['first_name'] = request.form['first_name']
     - Avoids having to set up a dictionary, and makes it simple for us to pass in the jinja tags directly just as session.first_name or the names we would be using from SQL database

 - GET is a MEGAPHONE to BLARE information through the URL
     - a tags and navigational buttons are GET requests generally
 - POST is silent envelope to PASS as COOKIE thanks to SESSION
     - POST should MOSTLY be ACTION ROUTE and Redirect
          - doesn't always hold the other way

OPTIONAL EVENING DEMONSTRATION DAY 5!!
 - https://www.youtube.com/watch?v=1jZO4UKjBXw&list=PLp3jkMF9o45ikcn7i_q_vOYNytJCuv8IB&index=23