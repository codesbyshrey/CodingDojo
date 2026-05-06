<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<!-- for Bootstrap CSS -->
<link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css" />
<!-- YOUR own local CSS -->
<link rel="stylesheet" href="/css/style.css"/>
<!-- LOCATED IN SRC/MAIN/RESOURCES/STATIC-->
<title>OMIKUJI</title>
</head>
<body>
	<div>
		<h1> Send an Omikuji!</h1>
		<form action="/submit" method="POST">
			<div>
				<label class="form-label"> Pick any number between 5 and 25 </label>
				<input class="form-control" type="number" min="5" max="25" name="number">
			</div>
			<div>
				<label class="form-label"> Enter the name of any city </label>
				<input class="form-control" type="text" name="city">
			</div>
			<div>
				<label class="form-label"> Enter the name of any real person </label>
				<input class="form-control" type="text" name="person">
			</div>
			<div>
				<label class="form-label"> Enter the name of any professional endeavor </label>
				<input class="form-control" type="text" name="profession">
			</div>
			<div>
				<label class="form-label"> Enter any kind of living thing (Patronus) </label>
				<input class="form-control" type="text" name="patronus">
			</div>
			<div>
				<label class="form-label"> Say something nice to someone </label>
				<input class="form-control" type="text" name="compliment">
			</div>
			<div>
				<label class="form-label"> Send to a fellow ninja </label>
				<input class="btn btn-primary" type="submit" value="Send">
			</div>
		</form>
	</div>

</body>

<!-- hint: use span tags -->
</html>