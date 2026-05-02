<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ page isErrorPage="true" %>  
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<!-- FOR BOOTSTRAP CSS -->
<link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css" />
<title> New Ninja </title>
</head>
<body>
	<div class="container">
		<h1>New Ninja</h1>
		<form:form action="" method="post" modelAttribute="ninja" class="form col-12">
			<div class="form-group mb-3">
				<form:label path="dojo" class="form-label">Dojo: </form:label>
				<form:select path="dojo" class="form-control">
					<c:forEach var="dojo" items="${dojos}">
						<form:option path="dojo" value="${dojo.id}"><c:out value="${dojo.name}"/></form:option>
					</c:forEach>
				</form:select>
			</div>
			<div class="form-group mb-3">
				<form:label path="firstName" class="form-label">First Name: </form:label>
				<form:input path="firstName" type="text" class="form-control"/>
			</div>
			<div class="form-group mb-3">
				<form:label path="lastName" class="form-label">Last Name: </form:label>
				<form:input path="lastName" type="text" class="form-control"/>
			</div>
			<div class="form-group mb-3">
				<form:label path="age" class="form-label">Ninja Age: </form:label>
				<form:input path="age" type="number" class="form-control"/>
			</div>
			<input type="submit" value="Create" class="btn btn-primary"/>
		</form:form>
	</div>
</body>
</html>