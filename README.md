# FloodWatch SL – Community Flood Risk Reporting System

**Module:** PROG211 Object-Oriented Programming 1, Limkokwing University of Creative Technology, Sierra Leone
**Domain:** Government – Citizen Complaint System (flood and drainage complaints)
**Author:** Charles Ensah

FloodWatch SL is a Python command-line application that helps communities in Sierra Leone, especially Freetown, report flooding, blocked drains and other water-related problems. It organises reports, ranks urgent incidents, tracks progress and highlights locations where problems keep coming back.

## Real-world problem
Flooding and poor drainage affect many Freetown communities every rainy season. Complaints are often scattered and unrecorded, so repeat problem areas are hard to see. FloodWatch SL gives a simple, structured way to record complaints and show where attention is needed first.

## Features
- Submit a flood report (location, problem type, description, severity, date)
- Automatic unique report IDs (`FW-0001`, `FW-0002`, ...)
- View all reports, search by ID or location
- Filter by severity or status
- Severity levels: Low, Medium, High
- Status tracking: Pending, Under Review, Action Taken, Resolved
- Priority ranking: unresolved High reports first, then Medium, then Low
- Recurring problem detection (locations with 2+ reports)
- Dashboard statistics (total, high-severity, unresolved, resolved)
- Input validation: menu choices and option numbers accept digits only; locations accept letters only (no numbers); descriptions must contain words; report IDs must match `FW-0000`; clear error messages and re-prompting; invalid data is also rejected inside the `FloodReport` class

## How the assignment tasks are met
| Task | Where |
|------|-------|
| **Task 1 – Classes and objects** | `FloodReport` (attributes + methods) and `ReportManager` interact in `main.py` |
| **Task 2 – One data structure** | `ReportManager.reports` is a **dictionary** keyed by report ID; `add_report()` and `display_all()` add and show records |
| **Tuples (optional)** | `SEVERITY_LEVELS`, `STATUSES`, `PROBLEM_TYPES` in `FloodReport` |
| **Task 3 – Methods** | Instance methods: `update_status()`, `display_info()`, `is_resolved()`. Class methods: `generate_id()`, `create()` (`@classmethod`) |

## Digital Public Goods (DPG) alignment
- **Open-source:** the code is public on GitHub under the MIT License, free to use, study and adapt.
- **Inclusive and accessible:** simple numbered menus, plain English, no special hardware, runs on any computer with Python.
- **Privacy-respecting:** no names, phone numbers or other personal data about the reporter are collected or stored. Reports describe places and problems only. Nothing is saved to disk when the program closes.
- **Modular and reusable:** the project is split into small modules (`report.py`, `manager.py`, `validation.py`) so other communities or districts can reuse or extend them.

## Project structure
```
floodwatch-sl/
├── main.py
├── floodwatch/
│   ├── __init__.py
│   ├── report.py        # FloodReport class
│   ├── manager.py       # ReportManager class
│   └── validation.py    # input validation helpers
├── README.md
├── LICENSE
└── .gitignore
```

## How to run
Requires Python 3.8 or newer. No extra libraries needed.
```
git clone https://github.com/<your-username>/floodwatch-sl.git
cd floodwatch-sl
python main.py
```
Every record in the program is one you enter yourself (option **1**); nothing is pre-loaded.

## Example usage (sample input/output)

**Priority ranking (option 8) after submitting several reports**
```
Priority ranking (unresolved reports)
--------------------------------------------------
1. FW-0001 | Kroo Bay | Flooding | High | Pending
2. FW-0003 | Kroo Bay | Overflowing Drain | High | Pending
3. FW-0002 | Susan's Bay | Blocked Drain | Medium | Pending
4. FW-0005 | Kroo Bay | Blocked Drain | Medium | Pending
```

**Recurring problem locations (option 9)**
```
Recurring problem locations (at least 2 reports)
--------------------------------------------------
Kroo Bay -> 3 reports (3 unresolved)
```

**Dashboard (option 10)**
```
===== DASHBOARD =====
Total reports       : 5
High-severity       : 2
Unresolved reports  : 4
Resolved reports    : 1
=====================
```

**Submitting a report (option 1)**
```
Community / location: Kissy Brook
Problem type:
  1. Flooding
  2. Blocked Drain
  ...
Choose a number (1-5): 2
Short description: Drain blocked by waste
Severity level:
  1. Low
  2. Medium
  3. High
Choose a number (1-3): 3

Report saved. Your report ID is FW-0006
```

## Screenshots of FloodWatch


<img width="486" height="364" alt="Screenshot 2026-10-09 183025" src="https://github.com/user-attachments/assets/0821a2c8-3b37-4b98-8198-d6f57400e15a" />



<img width="501" height="432" alt="Screenshot 2026-10-09 183113" src="https://github.com/user-attachments/assets/2564a2e5-94bf-4b8b-92eb-d96a454f45c3" />

```

```

## License
MIT License – see `LICENSE`.
