"""
Hector Jesus Mendez Santiago
Story:
You are going to make toast fast, you think that you should make multiple pieces of toasts and once. So, you try to make 6 pieces of toast.

Problem:
You forgot to count the number of toast you put into there, you don't know if you put exactly six pieces of toast into the toasters.

Define a function that counts how many more (or less) pieces of toast you need in the toasters. Even though you need more or less, the number will still be positive, not negative.

Examples:
You must return the number of toast the you need to put in (or to take out). In case of 5 you can still put 1 toast in:

5 --> 1
And in case of 12 you need 6 toasts less (but not -6):

12 --> 6



"""

def six_toast(num:int)->int:
    """
    Función que recibe un número, y retorna una cantidad que le hace falta o le sobra para tener
    una cantidad de 6
    :param num: número que se recibe
    :return : cantidad que sobra o falta
    """
    if num < 6:
        return 6 - num
    elif num > 6:
        return num - 6
    else:
        return 0
    # you code here


if __name__ == '__main__':
    num = int(input("Ingresa numero: "))
    print(six_toast(num))
