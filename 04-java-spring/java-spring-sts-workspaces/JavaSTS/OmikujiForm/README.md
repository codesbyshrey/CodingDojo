# Omikujiform

Spring form handling assignment.

Block: `Java and Spring Block`

## Revisit Notes

- Maven/Spring metadata is present; generated `target` output has been removed and can be rebuilt.

## Original README

## Omikuji Form

Omikuji Form is a **Spring Boot** application that simulates drawing a Japanese “omikuji” (fortune) using a web form and a results page.

### Overview

- **Goal**: Practice form handling, POST/redirect/GET, and displaying submitted data across multiple routes.
- **Core idea**: The user fills out a form (with numbers, location, person, hobby, etc.), submits it, and then receives a playful fortune page composed from their inputs.
- **Tech stack**: Java 17, Spring Boot 3, Spring MVC, JSP/JSTL.

### Project Structure

The Spring Boot project lives in the nested `OmikujiForm/` folder:

- `pom.xml` – Maven and Spring Boot configuration.
- `src/main/java` – Controller(s) for the form and the result page.
- `src/main/webapp/WEB-INF` – JSPs for the form and the generated fortune.
- `src/main/resources` – App configuration.

### How to Run Locally

1. **Prerequisites**
   - Java 17+
   - Maven
2. **Start the app**
   - `cd OmikujiForm`
   - `./mvnw spring-boot:run` or `mvnw.cmd spring-boot:run`
   - Visit `http://localhost:8080`.

### How to Use the App

1. Navigate to the form route (often `/omikuji`).
2. Fill out the requested fields (e.g., number, city, person’s name, activity, positive message).
3. Submit the form:
   - The controller typically stores the data in the session and redirects.
4. View the results page:
   - Your “fortune” is dynamically assembled using the submitted data.

### Design & Learning Focus

- **PRG pattern (Post/Redirect/Get)**
  - Form POSTs to a handler, then redirects to a GET route to render the result.
- **Session usage**
  - Data is temporarily stored in the HTTP session for the redirect.
- **Clean form UX**
  - Simple layout focusing on input clarity and playful copy for the fortune.

### Portfolio Highlights

- Great small demo of:
  - End‑to‑end request flow (form → controller → session → view).
  - Dynamic text generation from user input.
  - Spring MVC basics in a visually approachable context.
