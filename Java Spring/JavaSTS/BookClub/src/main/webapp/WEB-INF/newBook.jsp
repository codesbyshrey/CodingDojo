<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <!-- need c library, tag library, and error page -->
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ page isErrorPage="true" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<!-- FOR BOOTSTRAP CSS -->
<link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css" />
<title> NEWBOOK.JSP (book share)</title>
</head>
<body>
	<div class="container">
		<div class="navbar">
			<h1>Add a Book to Your Shelf!</h1>
			<a href="/books">Back to the Shelf!</a>
		</div>
		<form:form class="form" action="/books/new" method="POST" modelAttribute="newBook">
			<div class="form-group mb-3">
				<form:label class="form-label" path="title">Title</form:label>
				<form:errors class="text-danger" path="title"/>
				<form:input type="text" class="form-control" path="title"/>
			</div>
			<div class="form-group mb-3">
				<form:label class="form-label" path="author">Author</form:label>
				<form:errors class="text-danger" path="author"/>
				<form:input type="text" class="form-control" path="author"/>
			</div>
			<div class="form-group mb-3">
				<form:label class="form-label" path="thoughts">My Thoughts</form:label>
				<form:errors class="text-danger" path="thoughts"/>
				<form:textarea class="form-control" rows="4" cols="50" path="thoughts"/>
			</div>
			<form:input path="user" type="hidden" value="${user.id}"/>
			<input class="btn btn-primary" type="submit" value="Submit"/>
		</form:form>
	</div>
</body>
</html>