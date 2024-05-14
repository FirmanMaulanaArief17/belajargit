def f0():
    var=3

    def f1():
        #print(var)
        var=200

    f1()
    print(var)

f0()