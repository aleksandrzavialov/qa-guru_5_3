# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_lady(name, married, greeting):
    if married:
        print(f'Hello, {greeting} Mrs {name}.')  # Press Ctrl+F8 to toggle the breakpoint.
    else:
        print(f'Hi, {greeting} Ms {name}.')


print_lady('Sarah', False, 'lovely')
