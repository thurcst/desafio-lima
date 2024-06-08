def clean_data(data: dict) -> dict:
    """To clean this data will be necessary only remove whitespaces from the beginning and end.

    Args:
        data (dict): data to be clean

    Returns:
        data (dict): cleaned data
    """

    for key in data:
        if isinstance(data[key], list):
            data[key] = [x.strip() for x in data[key]]
        else:
            data[key] = data[key].strip()

    return data
