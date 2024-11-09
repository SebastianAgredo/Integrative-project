while True:

    num_1 = input("Digite un número entero\n")
    num_2 = input("Digite otro número entero\n")

    try:
        result = int(num_1)/int(num_2)


    except ValueError:
        print("Por favor solo ingrese números")

    except ZeroDivisionError:
        print("El segundo número evita que sea 0")

    except Exception as e:
        print("Se produjo un error, validación desconocida")

    

