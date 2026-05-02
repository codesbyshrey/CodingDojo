## Daikichi Path Variables

This project is a small **Spring Boot MVC** application that practices using **path variables** and basic routing. It exposes friendly “Daikichi” (good luck) messages using dynamic segments in the URL.

### Overview

- **Goal**: Get comfortable with Spring Boot controllers, `@PathVariable`, and returning simple views/strings.
- **Tech stack**: Java 17, Spring Boot 3, Spring MVC, JSP/JSTL (if views are used).
- **Example behavior** (typical for this assignment):
  - `GET /daikichi/travel/{city}` → “Congratulations! You will soon travel to {city}!”
  - `GET /daikichi/lotto/{number}` → Different message depending on whether `number` is even or odd.

### Project Structure

The Spring Boot project lives in the nested `DaikichiPathVariables/` folder:

- `pom.xml` – Maven configuration and Spring Boot dependencies.
- `src/main/java` – Controllers that define `@GetMapping` routes and handle path variables.
- `src/main/resources` – Application configuration and view templates if you are returning JSP pages.
- `target/` – Build artifacts.

Run all commands from inside the inner `DaikichiPathVariables` folder.

### How to Run Locally

1. **Install prerequisites**
   - Java 17+
   - Maven
2. **Start the app**
   - `cd DaikichiPathVariables`
   - `./mvnw spring-boot:run` (macOS/Linux) or `mvnw.cmd spring-boot:run` (Windows)
   - Open `http://localhost:8080` in your browser.

### How to Use the App

1. Hit the root or a base route, for example:
   - `http://localhost:8080/daikichi`
2. Try out the path‑variable routes:
   - `http://localhost:8080/daikichi/travel/Tokyo`
   - `http://localhost:8080/daikichi/lotto/7`
3. Adjust the values in the URL to see how the dynamic parts of the route affect the output.

### Design & Learning Focus

- **Controller‑centric design**
  - All behavior is implemented in simple controller methods using Spring annotations.
- **Path variables vs. query params**
  - Emphasizes REST‑style URLs (e.g., `/resource/{id}`) instead of only query strings.
- **Lightweight views**
  - Responses can be direct strings or JSP views; either way, the focus is on route handling, not heavy front‑end work.

### Portfolio Highlights

- Shows understanding of:
  - Spring Boot project setup and entry point.
  - Basic RESTful thinking and readable URLs.
  - `@RestController`/`@Controller` and `@PathVariable` usage.
- Great as a **micro‑demo** of clean, readable routing logic in Java.

