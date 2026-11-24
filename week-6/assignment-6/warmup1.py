def greet(name, greeting="Hello"):
    """Greets with a name and a customized message"""
    print(f"{greeting}! {name}")

# With only a name argument
greet("Patricia")
# With both a name and a custom greeting
greet("Olivia","Happy Birthday")
# With the greeting passed as a keyword argument
greet(name="Garry",greeting="Good morning")