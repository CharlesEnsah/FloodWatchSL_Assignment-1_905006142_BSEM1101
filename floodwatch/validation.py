"""Input validation: one set of rules used both when typing and inside the classes.

Each validate_* function returns the cleaned value, or raises ValueError
with a clear message explaining what is wrong.
"""

from datetime import date

ALLOWED_LOCATION_SYMBOLS = " '-.,"


def _is_ascii_digits(text):
    """True only for plain 0-9 (str.isdigit() also accepts things like '²')."""
    return text != "" and text.isascii() and text.isdigit()


# ---------- Validators (raise ValueError) ----------
def validate_location(text):
    """Letters only (plus spaces and ' - . ,). Numbers are not allowed."""
    text = " ".join(str(text).split())  # trim and collapse extra spaces
    if not text:
        raise ValueError("Location cannot be empty.")
    if any(ch.isdigit() for ch in text):
        raise ValueError("Location cannot contain numbers. Use letters only (e.g. Kroo Bay).")
    for ch in text:
        if not (ch.isalpha() or ch in ALLOWED_LOCATION_SYMBOLS):
            raise ValueError("Location contains an invalid symbol: '{}'.".format(ch))
    if sum(ch.isalpha() for ch in text) < 2:
        raise ValueError("Location must contain at least 2 letters.")
    if len(text) > 60:
        raise ValueError("Location is too long (maximum 60 characters).")
    return text


def validate_description(text):
    """Must be real text: at least 5 characters and contain letters (not only numbers/symbols)."""
    text = " ".join(str(text).split())
    if not text:
        raise ValueError("Description cannot be empty.")
    if not any(ch.isalpha() for ch in text):
        raise ValueError("Description must contain words, not only numbers or symbols.")
    if len(text) < 5:
        raise ValueError("Description is too short (at least 5 characters).")
    if len(text) > 300:
        raise ValueError("Description is too long (maximum 300 characters).")
    return text


def validate_report_id(text):
    """Report IDs look like FW-0001: 'FW-' followed by exactly 4 digits."""
    text = str(text).strip().upper()
    if not text:
        raise ValueError("Report ID cannot be empty.")
    if not text.startswith("FW-"):
        raise ValueError("Report ID must start with 'FW-' (example: FW-0001).")
    number = text[3:]
    if not _is_ascii_digits(number):
        raise ValueError("After 'FW-' the ID must be numbers only (example: FW-0001).")
    if len(number) != 4:
        raise ValueError("Report ID must have exactly 4 digits after 'FW-' (example: FW-0001).")
    return text


def validate_menu_number(text, low, high):
    """Must be a whole number between low and high. Returns it as an int."""
    text = str(text).strip()
    if not text:
        raise ValueError("Nothing entered. Please type a number from {} to {}.".format(low, high))
    if any(ch.isalpha() for ch in text):
        raise ValueError("Letters are not allowed here. Please type a number from {} to {}.".format(low, high))
    if not _is_ascii_digits(text):
        raise ValueError("Please type a whole number only (no spaces, symbols, decimals or minus signs).")
    number = int(text)
    if not low <= number <= high:
        raise ValueError("Number out of range. Choose between {} and {}.".format(low, high))
    return number


def validate_date(text):
    """Must be a real date in YYYY-MM-DD format and not in the future."""
    text = str(text).strip()
    try:
        parsed = date.fromisoformat(text)
    except ValueError:
        raise ValueError("Date must be a real date in YYYY-MM-DD format.")
    if parsed > date.today():
        raise ValueError("Report date cannot be in the future.")
    return parsed.isoformat()


def validate_choice(value, options, label):
    """Value must be exactly one of the allowed options."""
    if value not in options:
        raise ValueError("Invalid {}: {}. Allowed: {}.".format(label, value, ", ".join(options)))
    return value


# ---------- Input helpers (keep asking until valid) ----------
def ask(prompt, validator):
    """Ask repeatedly until `validator` accepts the typed text."""
    while True:
        try:
            return validator(input(prompt))
        except ValueError as error:
            print("  Error:", error)


def get_location(prompt="Community / location: "):
    return ask(prompt, validate_location)


def get_description(prompt="Short description: "):
    return ask(prompt, validate_description)


def get_report_id(prompt="Report ID (e.g. FW-0001): "):
    return ask(prompt, validate_report_id)


def get_menu_number(prompt, low, high):
    return ask(prompt, lambda text: validate_menu_number(text, low, high))


def choose_option(title, options):
    """Show a numbered menu from a tuple and return the chosen option."""
    print("\n" + title)
    for number, option in enumerate(options, start=1):
        print("  {}. {}".format(number, option))
    choice = get_menu_number("Choose a number (1-{}): ".format(len(options)), 1, len(options))
    return options[choice - 1]
