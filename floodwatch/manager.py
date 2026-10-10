"""ReportManager: stores and manages FloodReport objects."""

from .report import FloodReport


class ReportManager:
    """Keeps all reports in ONE data structure: a dictionary {report_id: FloodReport}."""

    def __init__(self):
        self.reports = {}

    # ---------- Add / display ----------
    def add_report(self, location, problem_type, description, severity):
        """Create a report and store it. Returns the new report."""
        report = FloodReport.create(location, problem_type, description, severity)
        self.reports[report.report_id] = report
        return report

    def display_all(self):
        """Display every recorded report."""
        if not self.reports:
            print("No reports recorded yet.")
            return
        print("\nAll reports ({}):".format(len(self.reports)))
        for report in self.reports.values():
            report.display_info()
        print("-" * 50)

    # ---------- Search ----------
    def search_by_id(self, report_id):
        """Show the report with the given ID."""
        report = self.reports.get(report_id.strip().upper())
        if report is None:
            print("No report found with ID", report_id)
        else:
            report.display_info()
            print("-" * 50)

    def search_by_location(self, text):
        """Show reports whose location contains the search text (not case-sensitive)."""
        text = text.strip().lower()
        found = 0
        for report in self.reports.values():
            if text in report.location.lower():
                report.display_info()
                found += 1
        if found == 0:
            print("No reports found for that location.")
        else:
            print("-" * 50)
            print("{} report(s) found.".format(found))

    # ---------- Filter ----------
    def filter_by_severity(self, severity):
        """Show reports with the chosen severity."""
        found = 0
        for report in self.reports.values():
            if report.severity == severity:
                report.display_info()
                found += 1
        print("-" * 50)
        print("{} report(s) with severity {}.".format(found, severity))

    def filter_by_status(self, status):
        """Show reports with the chosen status."""
        found = 0
        for report in self.reports.values():
            if report.status == status:
                report.display_info()
                found += 1
        print("-" * 50)
        print("{} report(s) with status {}.".format(found, status))

    # ---------- Status tracking ----------
    def update_status(self, report_id, new_status):
        """Update a report's status. Returns True if it worked."""
        report = self.reports.get(report_id.strip().upper())
        if report is None:
            return False
        return report.update_status(new_status)

    # ---------- Priority ranking ----------
    def show_priority_ranking(self):
        """List unresolved reports: High first, then Medium, then Low."""
        print("\nPriority ranking (unresolved reports)")
        print("-" * 50)
        rank = 1
        # Walk the severity tuple from the last item (High) to the first (Low).
        for severity in reversed(FloodReport.SEVERITY_LEVELS):
            for report in self.reports.values():
                if report.severity == severity and not report.is_resolved():
                    print("{}. {}".format(rank, report.summary()))
                    rank += 1
        if rank == 1:
            print("No unresolved reports.")

    # ---------- Recurring problems ----------
    def detect_recurring(self, minimum=2):
        """Highlight locations that have at least `minimum` reports."""
        print("\nRecurring problem locations (at least {} reports)".format(minimum))
        print("-" * 50)
        found = False
        for report in self.reports.values():
            key = report.location.lower()
            count = 0
            unresolved = 0
            first_match = None
            for other in self.reports.values():
                if other.location.lower() == key:
                    count += 1
                    if not other.is_resolved():
                        unresolved += 1
                    if first_match is None:
                        first_match = other
            # Only print each location once (on its first report).
            if first_match is report and count >= minimum:
                print("{} -> {} reports ({} unresolved)".format(
                    report.location, count, unresolved))
                found = True
        if not found:
            print("No recurring problem locations found.")

    # ---------- Dashboard ----------
    def dashboard(self):
        """Show summary statistics."""
        total = len(self.reports)
        high = 0
        resolved = 0
        for report in self.reports.values():
            if report.severity == "High":
                high += 1
            if report.is_resolved():
                resolved += 1
        print("\n===== DASHBOARD =====")
        print("Total reports       :", total)
        print("High-severity       :", high)
        print("Unresolved reports  :", total - resolved)
        print("Resolved reports    :", resolved)
        print("=====================")
