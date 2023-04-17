<!-- Here we have to import the Date class. -->
<!-- You will put the import in the first line of the jsp tag. Use the import attribute -->
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="java.util.Date"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Demo JSP</title>
    </head>
<body>
	<div class="container">
		Hello World
	</div>
    <!-- Inserting a for loop into your jsp -->
    <% for(int i = 0; i < 5; i++) { %>
        <h1><%= i %></h1>
    <% } %>
    <p>The time is: <%= new Date() %></p>
    
    <h2>Two plus two is: </h2>
    <h3> <c:out value="${2+2}"/> </h3>
    
    <!-- three config steps before data from controller can pass to jsp -->
    <!-- create src/main/webapp/WEB-INF -->
    
</body>
</html>
