// should be default
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>

// allows us to use C:out tags
// example <c:out value = "${data}"/>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

// fmt library usually to format date and time
// resorces here ==
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt"%>

// why do i have this here??
<%@ page import="java.io.*,java.util.*"%>

// to use the form:from tag
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>

// on the edit jsp
<%@ page isErrorPage="true" %>

//in the head for bootstrap
<link rel="stylesheet"
	href="/webjars/bootstrap/4.5.2/css/bootstrap.min.css" />
<script src="/webjars/jquery/3.5.1/jquery.min.js"></script>
<script src="/webjars/bootstrap/4.5.2/js/bootstrap.min.js"></script> 


<input type="hidden" name="_method" value="put"/>

<form:form action="/shows/new" method="post" modelAttribute="newShowPlus">
    <div class="form-group">
        <label>Title</label>
        <form:input path="title" cla-ss="form-control" />
        <form:errors path="title" class="text-danger" />
    </div>
    <div class="form-group">
        <label>Network</label>
        <form:input path="network" class="form-control" />
        <form:errors path="network" class="text-danger" />
    </div>
    <input type="submit" value="Add Show" class="btn btn-primary" />
</form:form>



<form action="/donation/new" method="post">
    <div class="form-group">
        <label>Donation Name</label>
        <input type="text" name="donationName" class="form-control" />
    </div>
    <div class="form-group">
        <label>Quantity</label>
        <input type="number" name="quantity" class="form-control" />
    </div>
    <div class="form-group">
        <label>Donor</label>
        <input type="text" name="donor" class="form-control" />
    </div>
    <input type="submit" value="Add Donation" class="btn btn-primary" />
</form>




<table class="table table-dark">
  <thead>
    <tr>
      <th scope="col">id</th>
      <th scope="col">First name</th>
      <th scope="col">Last name</th>
      <th scope="col">Age</th>
    </tr>
  </thead>
  <tbody>
    <c:forEach items="${dojo.ninjas}" var="ninja">
    <tr>
			<td>${ninja.id}</td>
			<td>${ninja.firstName}</td>
			<td>${ninja.lastName}</td>
			<td>${ninja.age}</td>
    </tr>
	</c:forEach>
  </tbody>
</table>