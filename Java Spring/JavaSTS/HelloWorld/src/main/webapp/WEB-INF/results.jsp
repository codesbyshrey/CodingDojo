<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
    
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title> FORM RESULTS </title>
</head>
<body>
	<h1>
		Email: <c:out value="${email }" />
	</h1>
	<h3>
		Password: <c:out value="${password }" />
	</h3>
</body>
</html>