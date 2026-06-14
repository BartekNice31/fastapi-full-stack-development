class Pydantic:
    def is_valid(self,text):
        if 'admin' in text:
            return False
        return True
    
class Starlette:
    def is_valid(self,text):
        return True
    
class FastAPI(Pydantic,Starlette):
    pass

f=FastAPI()
print(FastAPI.__mro__)
print(f.is_valid('admin'))