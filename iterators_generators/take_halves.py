def solution():
    def integers():
        number = 1
        
        while True:
            yield number
            number += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        return [next(seq) for _ in range(n)]
        
    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

take = solution()[0]
halves = solution()[1]
print(take(0, halves()))


"""def solution():
    def integers():
        number = 1
        
        while True:
            yield number
            number += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        for _ in range(n):
            yield next(seq)
        
    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(list(take(5, halves())))

take = solution()[0]
halves = solution()[1]
print(list(take(0, halves())))"""