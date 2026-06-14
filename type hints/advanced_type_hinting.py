from typing import List,Dict,Tuple,Union,Optional,Callable

class Job:
    def __init__(self,title:str='',description:Optional[str]=None)->None:
        self.title=title
        self.description=description
    def __repr__(self):
        return self.title

job1=Job("Manager","job manager")
job2=Job("Engineer")

price:List[int]=[12,23,233,22,22,21]
price:Tuple[int]=(1,2,5)
price:Dict[str,int]={'price1':10,'price2':20,'price3':30}

prices:List[Union[int,float]]=[20,20.5,21.6,24.5]

print(prices)
x:List[int | float]=[1,1.22,2.4,2]
print(x)

def inr_to_usd(value:float)->Union[float,None]:
    try:
        f=75
        value=value/f
        return value
    except TypeError as te:
        return None

print(inr_to_usd(200))
print(inr_to_usd('20'))

def smart_divider(func:Callable[[int,int],float]):
    def inner(a,b):
        if b==0:
            print("decorator- division by 0")
            return None
        return func(a,b)
    return inner

@smart_divider
def divider(a,b):
    print(f"result division a/b={a/b}")

print(divider(10,0))

Image=List[List[int]]
ImageFloat=List[List[float]]

def flatten_image(picture:Image)->List:
    flat_list=[]
    for list in picture:
        for item in list:
            flat_list.append(item)
    return flat_list

def flatten_image_float(picture:ImageFloat)->List:
    list_flatten=[]
    for list in picture:
        for item in list:
            list_flatten.append(item)
    return list_flatten

print(flatten_image([[1,2,3],[4,5,6]]))
print(flatten_image([[2,5],[3,6],[4,7]]))

print(flatten_image_float([[2.0,2.1],[2.4,2.6],[20.4,2.11]]))
