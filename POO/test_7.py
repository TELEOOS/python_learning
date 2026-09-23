class A:
    pass


class B:
    pass


x = A()
y = B()
z = A

print(isinstance(x, A)) #return True car x est une instance de la classe A
print(isinstance(x, B)) #return False x est une instance de la classe A pas B
print(isinstance(z, A)) # return False z est la classe A et non une instance de la classe A
print(type(z)) #return type
print(type(z()))#return une instance !