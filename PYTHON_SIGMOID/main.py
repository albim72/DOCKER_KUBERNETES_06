import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

if __name__ == '__main__':
    x = float(input("Podaj wartość x: "))
    print(f"wartość funkcji sigmoid dla x = {x} -> {sigmoid(x):.2f}")
