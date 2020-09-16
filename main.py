'''

	Transformar un loop a una funcion recurriste
Dentro de la función mete un if con la misma condición  que llevaría el while del for
Dentro del if anterior se requiere otro if
En el if interno se llama a la función recursiva y en el else se regresa el resultado
El llamado de la función recursiva debe regresarse
El llamado recursivo debe tener un return para  que el resultado final se regrese en cadena

'''


def main():
    def foo(word):
        s = set()
        for c in word:
            if c not in s:
                s.add(c)
            else:
                return c

    def bar(word, index, s):
        if index >= 0:
            if word[index] not in s:
                s.add(word[index])
                return bar(word, index - 1, s)
            else:
                return word[index]

    def baz(word, s, index=0):
        if index < len(word):
            if word[index] not in s:
                s.add(word[index])
                index += 1
                return baz(word, s, index)
            else:
                return word[index]

    word = "abca"
    s = set()
    print("foo", foo(word))
    print("bar", bar(word, len(word) - 1, s))
    print("baz", baz(word, s))


if __name__ == "__main__":
    main()
