example = "hello world"

def loc_ex():
    example = "this is local scope"
    return example

def loc_ex2():
    #example="apple"
    return example


print(example)
print(loc_ex())
print(loc_ex2())

an_int = 50


def inty():
    an_int = 100
    return an_int

print(inty())