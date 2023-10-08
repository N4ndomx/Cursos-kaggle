def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    if zip_code.isdigit() and len(zip_code) == 5:
        return True
    else:
        return False
    pass

# Check your answer
q1.check()