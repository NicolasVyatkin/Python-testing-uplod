# Convert Date  - add new solutions later

# This function should take a date string in the format dd/mm/yyyy and convert it to the format yyyy-mm-dd.
# If the input is not in the correct format, the function should return an error message "Error: Invalid date.".

# example

# Input: String (str).

# Output: String (str).

# Examples:

# assert convert_date("25/12/2021") == "2021-12-25"
# assert convert_date("01/01/2000") == "2000-01-01"
# assert convert_date("15/06/1995") == "1995-06-15"
# assert convert_date("29/02/2020") == "2020-02-29"

# How it’s used:

# in databases, while migrating data from one system to another with different date format requirements;
# in date picker UI components, where user input might be in a different format;
# in reporting tools to standardize date formats across different data sources.
# Preconditions:

# the input should be a string: date ∈ string;
# the input should match the pattern: dd/mm/yyyy, where 01 ≤ dd ≤ 31, 01 ≤ mm ≤ 12, and 1900 ≤ yyyy ≤ 2100.

################################################ SOLUTION#####################################################
from datetime import date


def convert_date(data: str) -> str:
    try:
        data_list = data.split('/')[::-1]
        start_date = date(int(data_list[0]), int(
            data_list[1]), int(data_list[2]))

# extract information such as the year, month, and day
    # year = start_date.year
    # month = start_date.month
    # day = start_date.day

# get the day of the week (Note: Monday is coded as 0, and Sunday as 6)
    # weekday = start_date.weekday()

# the date can be formatted as a string if needed
        date_str = start_date.strftime('%Y-%m-%d')
    # date_format = '%m/%d/%Y'
    # date_str = '-'.join(date.split('/')[::-1])
    # new_date = datetime.strftime(date_str, date_format)
    except:
        if ValueError:
            date_str = 'Error: Invalid date.'

    return date_str


print("Example:")
print(convert_date("25/12/2021"))
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
