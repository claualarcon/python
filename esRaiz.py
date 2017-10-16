print("Valores que anulan el Polinomio X^2 + 5X + 6 son: ")
cuenta =0
for i in range(-10,11):
    cuenta= (i**2 + 5*i + 6)
    if (cuenta == 0):
        print(f"El numero {i} es raiz")
    else: 
        print(f"El numero {i} no es raiz")