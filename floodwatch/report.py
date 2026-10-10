"""The FloodReport class: one community report about a flood or drainage problem."""

from datetime import date

from .validation import (
    validate_location, validate_description, validate_report_id,
    validate_date, validate_choice,
)


class FloodReport:
    """A single report. No personal data about the reporter is stored (DPG: privacy-respecting)."""

    # Tuples: fixed options that must never change while the program runs.
    SEVERITY_LEVELS = ("Low", "Medium", "High")
    STATUSES = ("Pending", "Under Review", "Action Taken", "Resolved")
    PROBLEM_TYPES = (
        "Flooding",
        "Blocked Drain",
        "Overflowing Drain",
        "Damaged Drainage",
        "Other",
    )

    # Class attribute shared by every report; used to build unique IDs.
    _next_number = 1

    def __init__(self, report_id, location, problem_type, description,
                 severity, report_date, status="Pending"):
        # Every value is checked here, so a bad report can never be created,
        # no matter where the data comes from.
        self.report_id = validate_report_id(report_id)
        self.location = validate_location(location)
        self.problem_type = validate_choice(problem_type, self.PROBLEM_TYPES, "problem type")
        self.description = validate_description(description)
        self.severity = validate_choice(severity, self.SEVERITY_LEVELS, "severity level")
        self.report_date = validate_date(report_date)
        self.status = validate_choice(status, self.STATUSES, "status")

    # ---------- Class methods ----------
    @classmethod
    def generate_id(cls):
        """Create the next unique report ID, e.g. FW-0001."""
        report_id = "FW-{:04d}".format(cls._next_number)
        cls._next_number += 1
        return report_id

    @classmethod
    def create(cls, location, problem_type, description, severity):
        """Build a new report with an automatic ID, today's date and Pending status."""
        report_id = cls.generate_id()
        try:
            return cls(report_id, location, problem_type, description,
                       severity, date.today().isoformat())
        except ValueError:
            cls._next_number -= 1  # do not waste an ID on a rejected report
            raise

    # ---------- Instance methods ----------
    def update_status(self, new_status):
        """Change the report status. Returns True if the status was valid."""
        if new_status not in self.STATUSES:
            return False
        self.status = new_status
        return True

    def is_resolved(self):
        """True when the report has been resolved."""
        return self.status == "Resolved"

    def display_info(self):
        """Print every detail of this report."""
        print("-" * 50)
        print("Report ID   :", self.report_id)
        print("Date        :", self.report_date)
        print("Location    :", self.location)
        print("Problem     :", self.problem_type)
        print("Severity    :", self.severity)
        print("Status      :", self.status)
        print("Description :", self.description)

    def summary(self):
        """One-line summary used in rankings and search results."""
        return "{} | {} | {} | {} | {}".format(
            self.report_id, self.location, self.problem_type,
            self.severity, self.status)
