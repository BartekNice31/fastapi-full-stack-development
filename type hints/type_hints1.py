from typing import List,Tuple,Dict,Union,Callable

def smart_divider(func:Callable[[int,int],float]):
    def inner(a,b):
        if b==0:
            print('division by 0')
            return None
        return func(a,b)
    return inner 

@smart_divider
def divider(a,b):
    print(a/b)

divider(10,0)

def total_price(price1:float,price2:float)->str:
    print(f"Price1: {price1} Price2: {price2} sum: {price1+price2}")
    return f'total price: {price1+price2}'

print(total_price('20','10')) 

def inr_to_usd(value:float)->Union[float,None]:
    try:
        factor=75
        value=value/factor
        return value
    except TypeError:
        return None
    
Image=List[List[int]]

def flatten_image(picture:Image)->List:
    flatten_list=[]
    for list in picture:
        for item in list:
            flatten_list.append(item)
    return flatten_list
print(inr_to_usd('10'))
print(flatten_image([[1,2,3],[4,5,6],[7,8,9],[10]]))