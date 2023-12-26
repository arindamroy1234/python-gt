def fuction_sample(param):
    a = 2
    print(str(param) + str(2))

def fuction_two(num1=7, num2=8):
    #print(num1 * num2)
    c = num1 * num2
    return c

fuction_sample("sam")


product = fuction_two(2)
print(product)

def func_vol(w, h):

    l = float(input("enter the length:"))
    vol = l * w * h
    print(round(vol, 2))

func_vol(2, 3)

