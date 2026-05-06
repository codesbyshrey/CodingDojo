# Arbotrary Copy

Flask/MySQL project variant kept as a source-different copy.

Block: `Python, Flask, and Django Block`

## Contents

- `arbotrary`: Flask/MySQL project variant kept as a source-different copy.

## Original README

## Arbotrary (Flask Red/Black Belt)

Arbotrary is a **Flask web application** built as a belt‑level project. It centers around managing trees and related data (for example, users, trees, and their attributes) with a full relational database backing.

### Overview

- **Goal**: Demonstrate end‑to‑end proficiency with Flask, Jinja templates, MySQL, and CRUD patterns.
- **Core idea**: Allow authenticated users to create, view, edit, and possibly “like” or interact with tree entries in an arborist‑themed application.
- **Tech stack**: Python (Flask), Jinja2 templates, MySQL (via an ORM or raw queries), HTML/CSS/JS.

### Project Structure

The actual app lives in the nested `arbotrary/` folder:

- `server.py` – Flask entry point and route registration.
- `flask_app/` – Application package:
  - Models, controllers, and templates (Jinja HTML files).
- `arbotrary_db.mwb` – MySQL Workbench model of the database schema.
- `Pipfile` / `Pipfile.lock` – Python dependencies.
- Wireframe PNGs – Visual design references for layout and flows.

### How to Run Locally

1. **Install prerequisites**
   - Python 3.x
   - pipenv (or convert the Pipfile to `requirements.txt`).
   - MySQL server with a database created to match the `.mwb` schema.
2. **Set up the environment**
   - `cd arbotrary/arbotrary`
   - `pipenv install`
   - Configure your DB connection in the app’s configuration (usually within `flask_app/__init__.py` or a config module).
3. **Initialize the database**
   - Use `arbotrary_db.mwb` / exported SQL to create the schema and tables.
4. **Run the app**
   - `pipenv run python server.py`
   - Visit `http://localhost:5000` in your browser.

### How to Use the App

1. Register or log in (if auth is enabled in this version).
2. Create a tree entry, specifying attributes such as species, location, and description.
3. Browse the list of trees and click into detail pages.
4. Edit or delete trees you own; optionally interact with others’ trees depending on the feature set (likes, comments, etc.).

### Design & Architecture Notes

- **Database‑driven**
  - Schema is designed in MySQL Workbench (`.mwb` files) and implemented in the app.
- **Flask blueprints or modularization**
  - Code is separated into routes, models, and templates for maintainability.
- **Wireframe‑driven UI**
  - The included PNGs guide the layout and look‑and‑feel of the finished pages.

### Portfolio Highlights

- Serves as a **flagship Flask project**:
  - Full CRUD.
  - Authentication and authorization (typical for belt assignments).
  - Real SQL schema and ERD design.
- Demonstrates your ability to take a concept from **wireframe + schema → working application**.
