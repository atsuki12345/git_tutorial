def cal_fibonacci(fn1,fn2,top):
    if top < 1:
        return fn1
    return cal_fibonacci(fn2,fn1+fn2,top-1)

def stepsToTheTop(top):
    #ここから書きましょう
    return cal_fibonacci(1,1,top)