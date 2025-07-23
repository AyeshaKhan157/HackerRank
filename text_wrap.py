import textwrap

def wrap(string, max_width):
    wrapped_lines = textwrap.wrap(string, max_width)
    return '\n'.join(wrapped_lines)

if __name__ == '__main__':
    string, max_width = input("enter alphabets"), int(input("enter number"))
    result = wrap(string, max_width)
    print(result)