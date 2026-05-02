## Registration

Registration is a small **HTML form** project (with the option to add CSS/JS) that focuses on collecting structured user data in a clear, accessible layout.

### Overview

- **Goal**: Practice building a registration form with proper labels, input types, and grouping.
- **Core idea**: Capture typical registration fields such as name, email, password, confirmation, and possibly additional profile information.
- **Tech stack**: HTML5 (with CSS for styling if extended).

### Project Structure

The project files live in the nested `Registration/` folder:

- `index.html` – Registration form markup.

You can expand this project by adding a dedicated `style.css` and client‑side validation.

### How to Run Locally

1. Open `Registration/index.html` in your browser, or
2. Serve the folder with a small HTTP server (e.g., `python -m http.server`) and browse to the file.

### How to Use the Page

- Fill in the required fields in the form.
- Submit the form:
  - In this exercise, submission is typically for local validation practice rather than being wired to a backend.
- Experiment with:
  - HTML5 validation (e.g., `type="email"`, `required` attributes).
  - Different input types such as `password`, `checkbox`, `radio`, and `select`.

### Design Notes

- **Form usability**
  - Labels are associated with inputs via the `for` / `id` pattern.
  - Fields are ordered in a natural top‑to‑bottom flow.
- **Visual clarity**
  - Spacing between groups (e.g., personal info vs. login info) supports quick scanning.

### Portfolio Highlights

- Demonstrates:
  - Attention to form semantics and accessibility.
  - An understanding of user onboarding flows (registration as first contact).
  - A foundation you can later connect to backend validation and authentication.

