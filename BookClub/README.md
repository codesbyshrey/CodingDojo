## BookClub

This project is a full‑stack **Spring Boot Book Club** application built as a Coding Dojo core assignment. It showcases user authentication, form validation, relational data modeling, and JSP views styled with Bootstrap.

### Overview

- **Goal**: Allow users to register, log in, and manage a collection of books they are reading or recommending.
- **Core idea**: Each user can create books, see what others are reading, and view details for each entry in a shared “book club” library.
- **Tech stack**: Java 17, Spring Boot 3, Spring MVC, Spring Data JPA, MySQL, JSP/JSTL, Bootstrap, BCrypt for password hashing.

### Project Structure

The actual Spring project lives in the nested `BookClub/` folder:

- `pom.xml` – Maven configuration with Spring Boot, JPA, MySQL, JSP/JSTL, validation, and BCrypt dependencies.
- `src/main/java` – Controllers, services, and models for users and books.
- `src/main/resources/application.properties` – Database connection, Hibernate, and other environment settings.
- `src/main/webapp/WEB-INF` – JSP views and layout fragments rendered by the controllers.
- `target/` – Build output (safe to delete and regenerate with Maven).

Run all commands from inside the inner `BookClub` folder (not the zip root).

### How to Run Locally

1. **Install prerequisites**
   - Java 17+
   - Maven
   - MySQL server with a schema created for this app (for example `bookclub_schema`).
2. **Configure the database**
   - Open `src/main/resources/application.properties`.
   - Update:
     - `spring.datasource.url` – point to your MySQL database.
     - `spring.datasource.username` / `spring.datasource.password`.
3. **Build and run**
   - From this directory: `cd BookClub`
   - Package and run with Maven:
     - `./mvnw spring-boot:run` (macOS/Linux)
     - `mvnw.cmd spring-boot:run` (Windows)
   - The app typically runs on `http://localhost:8080`.

### How to Use the App

1. **Register / log in**
   - Visit the root URL and create a new account.
   - Passwords are validated and stored securely using BCrypt.
2. **Create a book**
   - After login, use the “Add Book” / “New Book” form.
   - Provide title, author, thoughts/description, and any other required fields.
3. **Browse the library**
   - View a table/list of all books created by you and other users.
   - Click into a book to see full details.
4. **Edit or delete (if implemented)**
   - If the assignment includes ownership, you can only edit/delete books you created.

### Design & Architecture Notes

- **Layered design**
  - **Models** represent `User` and `Book` entities mapped via JPA to MySQL tables.
  - **Repositories** handle CRUD operations using Spring Data JPA.
  - **Services** encapsulate business rules like registration, login, and permissions.
  - **Controllers** coordinate HTTP requests and map them to JSP views.
- **Validation first**
  - Uses Spring’s validation annotations (e.g. `@NotBlank`, `@Size`, `@Email`) to keep forms robust.
  - Errors are surfaced back into the JSPs with user‑friendly messages.
- **Security considerations**
  - Login flow uses BCrypt for password hashing.
  - Session‑based auth protects routes so only authenticated users can manage books.

### Portfolio Highlights

- Demonstrates a complete **CRUD + auth** workflow in Java/Spring.
- Shows comfort with:
  - Maven configuration and dependency management.
  - MVC patterns using controllers, services, and repositories.
  - JSP/JSTL for server‑side templating.
  - Integrating Bootstrap for responsive layout and styling.

### Possible Extensions

- Add comments or ratings on books from other users.
- Implement search and filtering (by author, title, or user).
- Add pagination for large book collections.
- Integrate profile pages showing a user’s personal bookshelf.

