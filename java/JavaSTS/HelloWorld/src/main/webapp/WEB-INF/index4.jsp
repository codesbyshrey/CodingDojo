<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>Dojo Page</title>
</head>
<body>
    <h1>Dojo Locations</h1>
    <c:forEach var="oneDojo" items="${dojosFromMyController}">
        <p><c:out value="${oneDojo}"></c:out></p>
    </c:forEach>
    
    <c:forEach var="person" items="${people}">
    <c:out value="${person.name}"/>
	</c:forEach>
	
	<c:forEach var="banana" items="${people}">
    <c:out value="${banana.name}"/>
	</c:forEach>
	
    
</body>
</html>
