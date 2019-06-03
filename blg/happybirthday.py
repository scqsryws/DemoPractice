# first way
'''
def sing(name=input("Please input name:")):
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday,dear {}".format(name))
    print("Happy Birthday to you!")


sing()
'''

# second way


def happy():
    print("Happy Birthday to you!")


def sing(name):
    happy()
    happy()
    print("Happy Birthday ,dear", name)
    happy()


sing(name="Mike")