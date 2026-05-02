## Bank Account (OOP Python)

This project is an object‑oriented **Python bank account system** that models accounts and users interacting with them.

### Overview

- **Goal**: Practice classes, methods, and instance interactions using a familiar banking metaphor.
- **Core idea**: Represent `BankAccount` behavior (deposit, withdraw, interest, etc.) and connect accounts to users in `user_account.py`.
- **Tech stack**: Python 3, standard library only.

### Project Structure

The main code lives in the nested `bankaccount/` folder:

- `bank_account.py` – Core `BankAccount` class and related logic.
- `user_account.py` – User class that holds one or more `BankAccount` instances and coordinates operations.

### How to Run Locally

1. Ensure Python 3 is installed.
2. From this directory run one of the scripts, for example:
   - `python bankaccount/bank_account.py`
   - or `python bankaccount/user_account.py` (depending on which file has the demo code in `if __name__ == "__main__":`).
3. Observe console output for:
   - Balance changes.
   - Interest application.
   - Transfer or multi‑account interactions (if implemented).

### Design & Learning Focus

- **Encapsulation**
  - Account behavior is bundled together in a class instead of loose functions.
- **Method chaining & returns**
  - Many belt‑style assignments practice returning `self` to enable chained calls.
- **Reusability**
  - A `User` can hold multiple accounts, showcasing composition.

### Portfolio Highlights

- Clear demonstration of:
  - OOP fundamentals in Python.
  - Domain‑driven thinking (modeling real‑world concepts as classes).
  - Clean, readable console‑driven behavior.

