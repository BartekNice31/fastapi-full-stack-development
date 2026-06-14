class InfiniteNaturalNumbers:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        num=self.num
        self.num=self.num+1
        return num

def return_values():
    yield 1
    yield 2
    yield 'three'

value=return_values()
print(value.__next__())
print(value.__next__())
print(value.__next__())

values=iter(InfiniteNaturalNumbers())
print(next(values))
print(next(values))

prices=[1,2,3,4,5,6,7,8,9,10]
prices_iterator=prices.__iter__()

first_price=prices_iterator.__next__()
print(f"first price: {first_price}")

try:
    while True:
        print(prices_iterator.__next__())
except StopIteration:
    print("Koniec")

def sensors_temperature_generator():
    yield f"temperature: {20.5}"
    yield f"temperature: {20.5}"
    yield f"temperature: {20.5}"
    yield f"temperature: {20.5}"

sensors=sensors_temperature_generator()
try:
    while True:
        print(sensors.__next__())
except StopIteration as si:
    print(si)

def even_numbers():
    # generate  the even_numbers < 20
    for i in range(0,20):
        if i%2==0:
            yield i

evenNumbers=even_numbers()
try:
    while True:
        print(evenNumbers.__next__())
except StopIteration:
    print("STOP!")