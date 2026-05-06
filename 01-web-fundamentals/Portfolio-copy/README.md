# Portfolio Copy

Intro portfolio page assignment.

Block: `Web Fundamentals`

## Contents

- `Portfolio`: Intro portfolio page assignment.

## Original README

## Portfolio

This project is a **personal portfolio landing page** implemented with semantic HTML. It introduces who you are, showcases your technologies, and links to example work and contact methods.

### Overview

- **Goal**: Present yourself as a developer with a clean, focused single‑page site.
- **Core features**:
  - Name and profile image.
  - Quick links to GitHub, LinkedIn, and email.
  - A **Technologies** table grouped by category (Front‑End, Python, JavaScript, Database, Concepts).
  - A section linking to “Day 1 Applications” and an embedded contact form.
- **Tech stack**: HTML5 (and optionally a separate CSS file if extended).

### Project Structure

The main project files live in the nested `Portfolio/` folder:

- `index.html` – The portfolio page with profile content, technology table, and contact form.
- `images/` – Profile picture and icon assets for social links.
- `assets/` – Linked pages such as `about.html` and any supporting content.

### How to Run Locally

1. Open `Portfolio/index.html` in a browser, or
2. Serve the folder via a simple static server to keep paths identical to production:
   - Example: `python -m http.server` from the `Portfolio` directory and visit `http://localhost:8000`.

### How to Use / Navigate

- Click the **GitHub**, **LinkedIn**, and **Email Me** links below your name to explore your online presence.
- Browse the **Technologies** table to see your toolset across the stack.
- Use the **Day 1 Applications** links to view early exercises or demos.
- Fill out the **contact form** to send a message (in a production setting this would be wired to a backend or email service).

### Design Notes

- **Layout & hierarchy**
  - Large name header followed by social links keeps the focus on identity first.
  - Technology table visually communicates breadth of skills in a compact way.
- **Interaction**
  - External links open in a new tab (`target="blank"`), so visitors keep the portfolio open.
  - Form labels and inputs are grouped for accessibility and ease of use.

### Portfolio Highlights

- A strong **“first impression”** page you can point to in resumes and profiles.
- Showcases:
  - Semantic HTML structure.
  - Thoughtful organization of skills and contact information.
  - Early attention to UX details like link behavior and form layout.
