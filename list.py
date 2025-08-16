#Working with List

def list_examples():
    print("List examples below")
    numbers = []
    numbers_exp = []

    for i in range(5):
        numbers.append(i)
        numbers_exp.append(i ** 2)
        pass

    print(f"Numbers: {numbers}")
    print(f"NumbersExp: {numbers_exp}")

    # List comprehension
    numbers = [i * 2 for i in range(5)]
    print(f"\nNumbers with comprehension: {numbers}\n\n")

    # With string
    words = ["Python", "C#", "Java", "JS", "C++"]

    upper_words = [word.upper() for word in words]
    lower_words = [word.lower() for word in words]

    print(f"words: {words} \nupper: {upper_words}\nlower: {lower_words}\n\n")

    # Other examples
    exp_dictionary = {x: x ** 2 for x in range(5)}

    print(f"ExpDictionary: {exp_dictionary}")

    set_comprehensions = {x % 3 for x in range(10)}

    print(f"setComprehensions: {set_comprehensions}")
    print("___________________________________")