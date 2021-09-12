import webbrowser


def main():
    webbrowser.open('https://www.python.org/dev/peps/pep-0008', new=2)


def some_loop():
    counter = 100
    while counter > 0:
        print("I will not do stupid robot job")
        counter -= 1


if __name__ == "__main__":
    # execute only if run as a script
    main()
    some_loop()
