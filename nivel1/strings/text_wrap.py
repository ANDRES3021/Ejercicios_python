import textwrap

def wrap(string, max_width):
    resultado = textwrap.TextWrapper(width=max_width).fill(string)
    return(resultado)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
