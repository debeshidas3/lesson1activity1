# Diwali greeting in Python style
def festival_of_lights():
    diyas = ["🪔" for _ in range(5)]
    rangoli = "🌸✨🌼✨🌸"
    message = (
        "May the light of each diya shine bright,\n"
        "And rangoli colours paint your home with delight.\n"
        "Just like Python’s loops bring structure and flow,\n"
        "Let joy, peace and prosperity in your life overflow."
    )
    return f"{''.join(diyas)} {rangoli} {''.join(diyas)}\n{message}\n{''.join(diyas)} {rangoli} {''.join(diyas)}"

print(festival_of_lights())


