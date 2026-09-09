# Brown Bag Films - Technical Test Submission

## Author

Prepared by **Leonid Ksenchuk**

## Requirements

- Python 3.10 or newer
- No third-party Python packages are required
- SQLite support is included with the standard Python installation through the `sqlite3` module

## Project Files

- `question1.py` - prints a circle-like shape using Python loops
- `question2.py` - refactors question 1 into a class-based implementation
- `question3.py` - performs Depth First Search and Breadth First Search traversal
- `question4.py` - creates an SQLite database from the Appendix A JSON structure
- `question5.py` - fixes the Python lambda late-binding issue
- `appendix_a.json` - valid JSON representation of Appendix A
- `README.md` - project overview
- `RUN_INSTRUCTIONS.md` - setup and run instructions

## How to Run

Open a terminal in the project directory:

```bash
cd brown_bag_films_technical_test
```

Check Python:

```bash
python3 --version
```

Run each task:

```bash
python3 question1.py
python3 question2.py
python3 question3.py
python3 question4.py
python3 question5.py
```

On Windows, if `python3` is not available, use:

```bash
python question1.py
python question2.py
python question3.py
python question4.py
python question5.py
```

## Question 4 Output

Running:

```bash
python3 question4.py
```

creates:

```text
production_files.db
```

The SQLite database is generated automatically from `appendix_a.json`.

No manual database setup is required.
