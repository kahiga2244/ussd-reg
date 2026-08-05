def menu(text, phone):

    data = text.split("*") if text else []

    step = len(data)

    if step == 0:

        return """CON Welcome to Land Registry

1. Register
2. Search
3. Exit
"""