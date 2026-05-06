<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1" %>
<%@ taglib prefix="form"uri="http://www.springframework.org/tags/form" %>
<!DOCTYPE html>
<html>
  <head>
    <link
      rel="stylesheet"
      href="/webjars/bootstrap/4.5.2/css/bootstrap.min.css"
    />
    <!-- FOR BOOTSTRAP CSS -->
    <script src="/webjars/jquery/3.5.1/jquery.min.js"></script>
    <script src="/webjars/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    <meta charset="ISO-8859-1" />
    <title> LOGINPAGE.JSP </title>
  </head>

  <body>
    <div class="container">
      <div class="row">
        <div class="col">
          <h1>Register</h1>
          <form:form
            action="/register/user"
            method="post"
            modelAttribute="user"
          >
            <div class="form-group">
              <label>User Name</label>
              <form:input path="userName" class="form-control" />
              <form:errors path="userName" class="text-danger" />
            </div>
            <div class="form-group">
              <label>Email</label>
              <form:input path="email" class="form-control" />
              <form:errors path="email" class="text-danger" />
            </div>
            <div class="form-group">
              <label>Password</label>
              <form:input path="password" class="form-control" />
              <form:errors path="password" class="text-danger" />
            </div>
            <div class="form-group">
              <label>Confirm Password</label>
              <form:input path="confirm" class="form-control" />
              <form:errors path="confirm" class="text-danger" />
            </div>
            <input
              type="submit"
              value="Register User"
              class="btn btn-primary"
            />
          </form:form>
        </div>
        <div class="col">
          <h1>login</h1>
          <form:form
            action="/login/user"
            method="post"
            modelAttribute="loginUser"
          >
            <div class="form-group">
              <label>Email</label>
              <form:input path="email" class="form-control" />
              <form:errors path="email" class="text-danger" />
            </div>
            <div class="form-group">
              <label>Password</label>
              <form:input path="password" class="form-control" />
              <form:errors path="password" class="text-danger" />
            </div>
            <input type="submit" value="Add Show" class="btn btn-primary" />
          </form:form>
        </div>
      </div>
    </div>
  </body>
</html>
