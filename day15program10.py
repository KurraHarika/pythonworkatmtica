def outer():
    print('oute function')
    def inner():
        print('inner function')
    inner()

outer()
