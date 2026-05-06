# Fruityloops

Spring MVC/JSP fruit display assignment.

Block: `Java and Spring Block`

## Revisit Notes

- Maven/Spring metadata is present; generated `target` output has been removed and can be rebuilt.

## Original README

## FruityLoops

FruityLoops is a small **Spring Boot MVC** application that focuses on rendering dynamic data (like a list of fruits and prices) in a JSP view using loops.

### Overview

- **Goal**: Practice passing data from a controller to a view and iterating over collections in JSP.
- **Core idea**: Display a table of fruit items, their quantities, and prices computed on the server.
- **Tech stack**: Java 17, Spring Boot 3, Spring MVC, JSP/JSTL.

### Project Structure

The Spring Boot project lives in the nested `FruityLoops/` folder:

- `pom.xml` – Maven configuration with Spring Boot and JSP dependencies.
- `src/main/java` – Controller(s) that build a list of fruit objects and pass them to the view.
- `src/main/webapp/WEB-INF` – JSP pages that loop through the list and render a table.
- `src/main/resources` – Application properties.

### How to Run Locally

1. **Prerequisites**
   - Java 17+
   - Maven
2. **Start the app**
   - `cd FruityLoops`
   - `./mvnw spring-boot:run` (or `mvnw.cmd spring-boot:run` on Windows)
   - Open `http://localhost:8080` in your browser.

### How to Use the App

- Visit the root or main route (commonly `/fruits` or `/`).
- The page will render a table of fruit names, quantities, and prices.
- If you adjust the data in the controller (e.g., add more fruits), the view automatically updates.

### Design & Learning Focus

- **Model + view binding**
  - Demonstrates how to pass a list of custom objects from controllers to JSP via the model.
- **Templating with loops**
  - Uses JSTL tags (such as `<c:forEach>`) or similar to iterate in the view.
- **Clean, presentable layout**
  - Simple table layout styled (optionally with Bootstrap) to highlight structured data.

### Portfolio Highlights

- Great short example of:
  - Data binding from server to UI.
  - Separating controller logic from view rendering.
  - Using loops in server‑side templates.
