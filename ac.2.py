def cube(number):
    return number*number*number

def by_three(number):

    if number %3 ==0:
        return cube(number)
    else:
        return False

print(by_three(9))
print(by_three(4))
print(by_three(3))
print(by_three(333333333333336969696969693333369369396693696963969396939693696396396396396393936936936939369639693696))
