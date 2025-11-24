def divide():
    print()
    try:
        num1 = float(input("Ingrese un número: "))
        num2 = float(input("Ingrese otro número: "))
        print("La división es: " + str(num1/num2))
    # except: 
    #     print("se ha producido un error") #NO RECOMENTABLE
    except ValueError:
        print("El valor ingresado no es correcto. Intente nuevamente.")
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    except Exception as e:
        print("se ha producido un error: " + str(e))
    finally:
        print("Cálculo finalizado")

divide()