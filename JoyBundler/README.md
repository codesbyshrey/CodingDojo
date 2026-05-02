## JoyBundler

JoyBundler is a **Spring Boot MVC** application that bundles together “joyful” travel or activity packages. It emphasizes routing, form handling, validations, and rendering lists/detail pages with JSP.

### Overview

- **Goal**: Practice building a slightly larger CRUD‑style Spring project with multiple views and forms.
- **Core idea**: Users can create, view, and explore different “bundles” (for example trips, experiences, or product packages) and see them summarized in a UI.
- **Tech stack**: Java 17, Spring Boot 3, Spring MVC, Spring Data JPA (if persistence is configured), JSP/JSTL, optionally Bootstrap.

### Project Structure

The Spring Boot project lives in the nested `JoyBundler/` folder:

- `pom.xml` – Spring Boot and JSP dependencies.
- `src/main/java` – Controllers, models (e.g., `Bundle`), services, and repositories.
- `src/main/webapp/WEB-INF` – JSP templates for listing bundles and creating/editing them.
- `src/main/resources` – App configuration, including database settings if using JPA.

### How to Run Locally

1. **Prerequisites**
   - Java 17+
   - Maven
   - MySQL (if the project is configured with JPA persistence)
2. **Configure database (if applicable)**
   - Edit `application.properties` with the correct JDBC URL, username, and password.
3. **Start the app**
   - `cd JoyBundler`
   - `./mvnw spring-boot:run` or `mvnw.cmd spring-boot:run`
   - Open `http://localhost:8080`.

### How to Use the App

1. Go to the main page to see existing bundles (if seeded).
2. Use the “New Bundle” or similar route to create a new joy bundle:
   - Fill in fields such as title, description, price, and dates.
3. View a bundle detail page to see more information.
4. Edit or delete bundles (if those features are implemented).

### Design & Architecture Notes

- **Domain modeling**
  - Bundles are represented as entities with fields like name, description, and tracking fields.
- **Form validation**
  - Uses Spring validation annotations on DTOs/entities to guard required fields.
- **Reusable layout**
  - JSPs likely share common navigation and styling to present JoyBundler as a cohesive mini‑product.

### Portfolio Highlights

- Represents a more complete Spring MVC app with:
  - Multiple pages and flows.
  - Validated form handling.
  - Potential database CRUD operations.
- Good demo of turning a simple concept into a “productized” experience.

