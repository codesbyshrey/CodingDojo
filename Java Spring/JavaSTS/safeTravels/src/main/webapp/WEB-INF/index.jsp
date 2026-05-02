<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>    
<%@ page isErrorPage="true" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
    
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<!-- FOR BOOTSTRAP CSS -->
<link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css" />
<title> SAFE TRAVELS CORE </title>
</head>
<body>
	<div class="container">
		<div class="row">
			<h1>Save Travels</h1>
			<table class="table table-striped">
				<thead>
					<tr>
						<th class="col-4">Expense</th>
						<th>Vendor</th>
						<th>Amount</th>
						<th>Actions</th>
					</tr>
				</thead>
				<tbody>
					<c:forEach var="expense" items="${expenses}">
					<tr>
						<td><a href="/expenses/${expense.id}"><c:out value="${expense.name}"/></a></td>
						<td><c:out value="${expense.vendor}"/></td>
						<td>$<fmt:formatNumber type="number" minFractionDigits="2" value="${expense.amount}"/></td>
						<td style= "display:flex; justify-content:space-around">
							<a href="/expenses/edit/${expense.id}">edit</a>
							<form action="/expenses/${expense.id}" method="post">
    							<input type="hidden" name="_method" value="delete">
    							<input class="btn btn-danger" type="submit" value="Delete">
							</form>
						</td>
					</tr>				
					</c:forEach>
				</tbody>
			</table>
		</div>
	
		<div class="row">
			<h2>Add an Expense: </h2>
			<form:form class="form" action="/expenses" method="post" modelAttribute="expense">
				<div class="form-group mb-3" >
					<form:label path="name">Expense Name: </form:label>				
					<form:errors class="text-danger" path="name"/>
					<form:input class="form-control" type="text" path="name"/>
				</div>
				<div class="form-group mb-3">
					<form:label path="vendor">Vendor: </form:label>
					<form:errors class="text-danger" path="vendor"/>
					<form:input class="form-control" type="text" path="vendor"/>
				</div>
				<div class="form-group mb-3">
					<form:label path="amount">Amount: </form:label>
					<form:errors class="text-danger" path="amount"/>
					<form:input class="form-control" type="number" path="amount"/>
				</div>
				<div class="form-group mb-3">
					<form:label path="description">Description: </form:label>
					<form:errors class="text-danger" path="description"/>
					<form:textarea class="form-control" rows="4" cols="50" path="description"/>
				</div>
				<input class="btn btn-primary" type="submit" value="Submit"/>
			</form:form>
		</div>
	</div>
</body>
</html>