def mymax(iterable, key = lambda x: x):
    max_x=max_key=None

    for x in iterable:
        if max_key is None or key(x) > max_key:
            max_x = x
            max_key = key(x)

    return max_x

def main():
    maxint = mymax([1, 3, 5, 7, 4, 6, 9, 2, 0])
    print("maxint: ", maxint)

    maxchar = mymax("Suncana strana ulice")
    print("maxchar: ", maxchar)

    maxstring = mymax([
    "Gle", "malu", "vocku", "poslije", "kise",
    "Puna", "je", "kapi", "pa", "ih", "njise"])
    print("maxstring: ", maxstring)

    D={'burek':8, 'buhtla':5}
    maxdict = mymax(D, D.get)
    print("maxdict: ", maxdict)

    names = [
    ("Marko", "Markovic"), ("Ana", "Anic"), ("Pero", "Peric"), ("Maja", "Majic"), 
    ("Iva", "Ivic"), ("Ivan", "Ivic"), ("Petar", "Petrovic"), ("Marta", "Martic"), 
    ("Luka", "Lukic"), ("Sara", "Saric"), ("Mia", "Mijic"), ("Toni", "Zvekavac"), 
    ("Toni", "Tonic"), ("Toni", "Tonovic")]

    lastname = mymax(names)
    print("lastname: ", lastname)

if __name__ == "__main__":
    main()