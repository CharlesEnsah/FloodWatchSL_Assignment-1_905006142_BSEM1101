"""FloodWatch SL - Community Flood Risk Reporting System (command-line menu)."""

from floodwatch import FloodReport, ReportManager
from floodwatch.validation import (
    get_location, get_description, get_report_id, get_menu_number, choose_option,
)

MENU = """
========== FloodWatch SL ==========
1. Submit a flood report
2. View all reports
3. Search by report ID
4. Search by location
5. Filter by severity
6. Filter by status
7. Update report status
8. Priority ranking
9. Recurring problem locations
10. Dashboard statistics
0. Exit
"""


def submit_report(manager):
    location = get_location("Community / location: ")
    problem_type = choose_option("Problem type:", FloodReport.PROBLEM_TYPES)
    description = get_description("Short description: ")
    severity = choose_option("Severity level:", FloodReport.SEVERITY_LEVELS)
    try:
        report = manager.add_report(location, problem_type, description, severity)
    except ValueError as error:  # safety net: the class rejected the data
        print("\nReport NOT saved:", error)
        return
    print("\nReport saved. Your report ID is", report.report_id)


def update_status(manager):
    report_id = get_report_id("Report ID (e.g. FW-0001): ")
    if report_id not in manager.reports:
        print("No report found with ID", report_id)
        return
    new_status = choose_option("New status:", FloodReport.STATUSES)
    manager.update_status(report_id, new_status)
    print("Status updated to", new_status)


def main():
    manager = ReportManager()
    try:
        while True:
            print(MENU)
            choice = get_menu_number("Select an option (0-10): ", 0, 10)

            if choice == 1:
                submit_report(manager)
            elif choice == 2:
                manager.display_all()
            elif choice == 3:
                manager.search_by_id(get_report_id("Report ID (e.g. FW-0001): "))
            elif choice == 4:
                manager.search_by_location(get_location("Location: "))
            elif choice == 5:
                manager.filter_by_severity(
                    choose_option("Severity level:", FloodReport.SEVERITY_LEVELS))
            elif choice == 6:
                manager.filter_by_status(
                    choose_option("Status:", FloodReport.STATUSES))
            elif choice == 7:
                update_status(manager)
            elif choice == 8:
                manager.show_priority_ranking()
            elif choice == 9:
                manager.detect_recurring()
            elif choice == 10:
                manager.dashboard()
            elif choice == 0:
                print("Thank you for using FloodWatch SL. Stay safe!")
                break
    except (KeyboardInterrupt, EOFError):
        print("\nInput closed. Thank you for using FloodWatch SL. Stay safe!")


if __name__ == "__main__":
    main()
