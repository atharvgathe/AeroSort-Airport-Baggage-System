# ✈️ AeroSort — Airport Baggage Management System

AeroSort is a Python-based Airport Baggage Management System developed as an academic **Data Structures and Algorithms (DSA) project**. It simulates baggage registration, tracking, searching, sorting, priority handling, and status management through a simple web interface.

Built using **Python, Flask, SQLite, HTML, and CSS**, the system demonstrates how fundamental data structures and algorithms can be applied to airport baggage management.

## 🚀 Features

- **Interactive Dashboard:** View baggage statistics and totals categorized by baggage status.
- **Baggage Management:** Register new baggage records, update existing information, and delete records.
- **Baggage Search:** Find baggage using Linear Search or Binary Search based on numeric tracking IDs.
- **Sorting Algorithms:** Organize baggage records using Bubble Sort, Insertion Sort, and Merge Sort.
- **Priority-Based Processing:** Process urgent and priority baggage ahead of normal baggage using a priority queue.
- **Persistent Storage:** Store baggage records in an SQLite database.
- **Sample Data:** Explore the system using predefined sample baggage records.
- **Responsive Interface:** Access the system through a clean web interface built with HTML and CSS.
- **Local Illustrations:** Use locally stored SVG illustrations for visual elements.

## 🛠️ Technologies Used

| Component | Technology |
|---|---|
| Programming Language | Python |
| Web Framework | Flask |
| Database | SQLite |
| Frontend | HTML5, CSS3 |
| Data Structures | Queues, Priority Queues, Dictionaries |
| Searching Algorithms | Linear Search, Binary Search |
| Sorting Algorithms | Bubble Sort, Insertion Sort, Merge Sort |
| Graphics | SVG |
| Development Environment | Visual Studio Code |

**Note:** The project does not use JavaScript, React, or an external database server.

## 🧠 Data Structures and Algorithms

AeroSort demonstrates the following DSA concepts:

| Concept | Application | Time Complexity |
|---|---|---|
| Queue | Manage baggage processing in FIFO order | O(1) enqueue/dequeue |
| Priority Queue | Handle urgent, priority, and normal baggage | Depends on implementation |
| Linear Search | Search baggage records sequentially | O(n) |
| Binary Search | Search sorted records by tracking ID | O(log n) |
| Bubble Sort | Sort baggage records | O(n²) average/worst case |
| Insertion Sort | Sort baggage records | O(n²) average/worst case |
| Merge Sort | Efficiently sort baggage records | O(n log n) |
| Dictionary / Hash Lookup | Access records using keys, where implemented | O(1) average |

*Complexities describe typical algorithmic behavior; actual performance depends on the implementation and input data.*

## 📂 Project Structure

```text
airport-baggage-python/
│
├── app.py                 # Flask application and routes
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
├── static/                # CSS, SVGs, and other static assets
├── database/              # Database-related files, if present
└── README.md              # Project documentation
```

*The directory structure above is illustrative. Adjust it to match the actual files and folders in your project.*

## ⚙️ Installation and Setup

### Prerequisites

- Python 3 installed
- Visual Studio Code or another code editor
- A web browser

### Run on Windows

**1. Download or clone the repository**

Open the project folder in Visual Studio Code.

**2. Open the terminal**

Select **Terminal → New Terminal**.

**3. Create a virtual environment**

```powershell
py -m venv .venv
```

**4. Activate the virtual environment**

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can run the project using the virtual environment's Python executable directly.

**5. Install dependencies**

```powershell
python -m pip install -r requirements.txt
```

**6. Start the application**

```powershell
python app.py
```

**7. Open AeroSort in your browser**

Navigate to:

[http://127.0.0.1:5000](http://127.0.0.1:5000)

The Flask development server will serve the application locally.

## 📋 How It Works

1. **Register baggage:** Add baggage information and its tracking ID.
2. **View the dashboard:** Monitor baggage records and their current statuses.
3. **Search baggage:** Locate records using Linear Search or Binary Search.
4. **Sort records:** Organize baggage data using the available sorting algorithms.
5. **Prioritize handling:** Process urgent baggage before lower-priority baggage.
6. **Manage records:** Update or delete baggage entries as required.

## 🎯 Project Objectives

- Apply DSA concepts to a practical management scenario.
- Understand the implementation and performance of searching and sorting algorithms.
- Demonstrate FIFO queues and priority-based processing.
- Integrate Python application logic with a relational database.
- Build a functional web interface using Flask, HTML, and CSS.
- Understand how structured data processing can improve baggage tracking workflows.

## 🎓 DSA Viva Preparation

**1. What is a queue?**

A queue is a linear data structure that follows FIFO (First In, First Out).

**2. Why use a priority queue?**

A priority queue processes elements according to their assigned priority instead of relying only on insertion order.

**3. What is the difference between Linear Search and Binary Search?**

Linear Search checks elements sequentially, while Binary Search repeatedly divides a sorted search range in half.

**4. Why is Merge Sort more efficient for large datasets?**

Merge Sort uses divide and conquer and runs in O(n log n) time.

**5. Why is SQLite used?**

SQLite provides lightweight, persistent database storage without requiring a separate database server.

**6. Why use Flask?**

Flask connects the Python application logic to web routes and HTML templates.

## 🔮 Future Enhancements

- Add baggage location and destination tracking.
- Introduce baggage status filters and advanced search.
- Add user authentication and role-based access.
- Generate baggage processing reports.
- Visualize baggage processing statistics.
- Integrate simulated airline and flight information.

## ⚠️ Disclaimer

AeroSort is an educational simulation created for academic purposes. It does not connect to real airport, airline, or baggage tracking systems. Use fictional passenger information when testing the application.

## 👨‍💻 Project Information

**Project:** AeroSort — Airport Baggage Management System  
**Domain:** Data Structures and Algorithms  
**Application Type:** Python-based Web Application  
**Purpose:** Academic Mini Project

---

*Built to demonstrate how data structures and algorithms can make baggage management more organized and efficient.*
