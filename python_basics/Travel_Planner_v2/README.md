# Ultimate Travel Planner CLI - Version 2

## Overview

This is **Version 2** of the CLI Travel Planner app. Unlike Version 1, this version focuses on **practicing core Python concepts** while building a functional, persistent, modular CLI application.

The app allows users to:

- Create, view, delete, and search trips
- Track trip expenses
- View summary statistics
- Persist trip data using JSON
- Log key actions

No object-oriented programming was used; all functionality is implemented with functions, loops, conditionals, and core Python data structures.

---

## Project Structure

- `main.py` — CLI entry point and menu loop
- `trip_manager.py` — Functions for trip creation, deletion, search, view, load/save JSON
- `utils.py` — Input validation and helper functions
- `data.json` — JSON database for storing trips
- `log.txt` — Log of trip actions

---

## Features Implemented

### Trip Management

- Create trips with fields:
  - `id` (unique timestamp string)
  - `destination`
  - `budget`
  - `travel_date` (YYYY-MM-DD)
  - `tags` (list of strings)
  - `notes`
  - `expenses` (list of floats)
- Delete trips by Trip ID
- Search trips by destination or tags
- View all trips in a formatted table
- Track and add expenses per trip
- Show total spent and remaining budget per trip

### Persistence & File Handling

- Store all trips in `data.json` (create if missing)
- Load trips safely with error handling
- Append new trips without overwriting
- Maintain action log in `log.txt`
- Handle file reading, writing, and appending

### CLI Flow

- Main menu loop using `while` and `if...else`
- Graceful exit with `KeyboardInterrupt`
- Input validation loops for floats, dates, and non-empty strings

---

## Python Concepts Practiced

### Variables & Data Types

- Strings, integers, floats, lists, tuples, sets, dictionaries
- Booleans for validation and flow control

### Operators & Math

- Arithmetic and comparison operators
- `math.ceil()`, `math.floor()` and other math functions

### Control Flow

- If...Else and Match statements
- While loops for menus and validation
- For loops for iterating trips, tags, and expenses

### Functions & Modules

- Modular functions for all trip actions
- Parameter passing, return values, reusable helpers
- Python standard modules: `datetime`, `os`, `json`, `math`, `array`

### Strings & Formatting

- f-strings for formatted output
- String methods: `.upper()`, `.lower()`, `.split()`, `.strip()`

### User Input & Validation

- Loops and try-except for robust input handling
- Reject negative budgets, invalid dates, or empty strings

### JSON & File Handling

- Reading and writing JSON files
- Creating, appending, and deleting files
- Error handling for file operations

### Arrays & Iterators

- Used array module for numeric lists (optional)
- Iteration with for loops and iterator patterns

### Exception Handling

- Handle ValueError, FileNotFoundError, and KeyboardInterrupt

---

## Summary

In Version 2, the Travel Planner CLI became a **modular, persistent, fully functional CLI app** while serving as a **practice ground for core Python fundamentals**.

By building this version, I practiced:

- Core data structures and types
- Loops, conditionals, and input validation
- File handling and JSON persistence
- Using Python standard modules
- CLI application flow and logging

This version prepares the foundation for more advanced upgrades like OOP, SQLite databases, and professional CLI tools in future versions.
