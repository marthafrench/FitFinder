def validate_size(size):
    """Validates if the provided size is a number and within a reasonable range."""
    try:
        size = int(size)
        if 0 < size < 50:  # Assuming size range is 1-50
            return True
        else:
            return False
    except ValueError:
        return False
