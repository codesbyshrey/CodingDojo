<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
 <%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
 
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Conditional JSTL Tags</title>
</head>
<body>
	<h1> Guess the number (secretNumber)</h1>
	<hr>
	<p> c:choose tags are basically switch statements </p>
	<p> c:when tags are basically case statements </p>
	<p> c:otherwise tags serve same as default (or else statement) </p>
	
	
	<c:if test = "${number<secretNumber}">
		<p><c:out value="Your number is too low."/></p>
	</c:if>
	<c:if test = "${number>secretNumber}">
		<p><c:out value="Your number is too high."/></p>
	</c:if>
	<c:if test = "${number==secretNumber}">
		<p style="color:green;"><c:out value="You got it!"/></p>
	</c:if>

	<c:if test = "${number!=secretNumber}">
		<p><c:out value="Try again."/></p>
	</c:if>
	
	<hr>
	<h2> using c:choose conditional JSTL tag</h2>
	<c:choose>
	<c:when test="${number<secretNumber}">
		<p><c:out value="Your number is too low."/></p>
	</c:when>
	<c:when test="${number>secretNumber}">
		<p><c:out value="Your number is too high."/></p>
	</c:when>
	<c:otherwise>
		<p><c:out value="You got it!"/></p>
	</c:otherwise>
</c:choose>
	

</body>
</html>