def greet(name: str) -> None:
    print(f"Hello {name}, Welcome to CCR.")
    """Prints the name of the person being greeted"""

def main():
    greet.greet("Michael")
print("Loaded greet module")
if __name__ == "__main__":
    main()