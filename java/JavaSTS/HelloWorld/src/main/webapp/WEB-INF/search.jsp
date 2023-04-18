<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
    
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title> search </title>
</head>
<body>
    
    <!--   ...   -->
    
    <form action="/search">
        <label>Search:</label>
        <input type="text" name="searchTerm">
        <input type="submit">
    </form>
    
<!--   ...   -->

    
    <!-- have to redirect to a page to ensure session stays in session -->
</body>
</html>