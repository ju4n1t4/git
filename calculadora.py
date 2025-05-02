# Calculadora básica que suma dos números

def sumar(a, b):
    return a + b

def main():
    print("Calculadora de suma")
    
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        resultado = sumar(num1, num2)
        print(f"El resultado de la suma es: {resultado}")
    
    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")

if __name__ == "__main__":
    main()

