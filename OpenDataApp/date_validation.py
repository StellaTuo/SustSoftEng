import re
from datetime import date, datetime

def validate_date(date_str):
    # check exact format
    if not re.fullmatch(r"\d{4}/\d{2}/\d{2}", date_str):
        print("Date must be in the format YYYY/MM/DD")
        return None

    try:
        parsed = datetime.strptime(date_str, "%Y/%m/%d").date()
        min_date = date(2014, 1, 1)
        max_date = date.today()

        if parsed < min_date:
            print("Date must be after 2014/01/01")
            return None

        if parsed > max_date:
            print("Date must not be in the future")
            return None

        return date_str

    except ValueError:
        print("Invalid date.")
        return None