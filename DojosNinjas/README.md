## Dojos & Ninjas

This project is a **Spring Boot CRUD** application that models a classic one‑to‑many relationship between **Dojos** and **Ninjas**. It is designed as a relational data and MVC practice assignment.

### Overview

- **Goal**: Practice setting up one‑to‑many relationships, using foreign keys, and rendering related data in views.
- **Core idea**: A dojo can have many ninjas; ninjas belong to exactly one dojo.
- **Tech stack**: Java 17, Spring Boot 3, Spring MVC, Spring Data JPA, MySQL, JSP/JSTL.

### Project Structure

The Spring Boot project lives in the nested `DojosNinjas/` folder:

- `pom.xml` – Spring Boot, JPA, MySQL, JSP dependencies.
- `src/main/java` – Models, repositories, services, and controllers for `Dojo` and `Ninja`.
- `src/main/resources` – Database config and view resolution.
- `src/main/webapp/WEB-INF` – JSP views for listing and creating dojos and ninjas.

### How to Run Locally

1. **Install prerequisites**
   - Java 17+
   - Maven
   - MySQL server and a schema created for this app.
2. **Configure the database**
   - Edit `src/main/resources/application.properties` to point at your MySQL instance.
3. **Start the app**
   - `cd DojosNinjas`
   - `./mvnw spring-boot:run` or `mvnw.cmd spring-boot:run`
   - Open `http://localhost:8080`.

### How to Use the App

1. **Create a dojo**
   - Use the “New Dojo” form to add a dojo record.
2. **Create a ninja**
   - Use the “New Ninja” form, selecting an existing dojo from a dropdown.
3. **Browse relationships**
   - Visit a dojo detail page to see all ninjas associated with that dojo.

### Design & Architecture Notes

- **Relational modeling**
  - `Dojo` has a `@OneToMany` relationship to `Ninja`.
  - `Ninja` has a `@ManyToOne` relationship back to `Dojo`.
- **Data integrity**
  - Forms ensure you can only create ninjas that are attached to valid dojos.
- **MVC separation**
  - Controllers are kept lean, delegating to services/repositories for database access.

### Portfolio Highlights

- Demonstrates the ability to:
  - Model and query relational data with JPA/Hibernate.
  - Build forms that bind to complex objects.
  - Render parent/child data structures in JSP views.
- A nice **showcase piece** for understanding database relationships in a Java web stack.

