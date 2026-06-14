from pydantic import BaseModel,Field
from typing import Optional,List
from enum import Enum
from datetime import datetime
import time

class Language(str,Enum):
    PYTHON="python"
    JAVA="java"
    C="c"
    CPLUSPLUS="c++"
    CSHARP="C#"

class Comment(BaseModel):
    text:Optional[str]=None

class Blog(BaseModel):
    title:str
    description:Optional[str]=None
    is_active:bool
    language:Language=Language.PYTHON
    comments:Optional[List[Comment]]
    create_at:datetime=Field(default_factory=datetime.now)

class TemperatureHumiditySensor(BaseModel):
    name:Optional[str]=None
    temperature:float
    humidity:float


class TypeSensor(str,Enum):
    HUMIDITY="humidity"
    TEMPERATURE="temperature"
    OPTIC="optic"

class Sensor(BaseModel):
    value:float
    name:Optional[str]=None
    type:TypeSensor
    time_measure:datetime=Field(default_factory=datetime.now)

class User(BaseModel):
    login:str
    password:str
    description:Optional[str]=None
    is_active:bool
    is_admin:bool
    created_at:datetime=Field(default_factory=datetime.now)

# print("Sensors")
# sensor1=Sensor(value=20.5,type=TypeSensor.TEMPERATURE)

# print(sensor1)
# time.sleep(2)
# sensor2=Sensor(value=200.5,name="Keyence optical sensor",type=TypeSensor.OPTIC)
# print(sensor2)
# print(sensor1.time_measure)
# print(sensor2.time_measure)

# print("blogs")
# blog1=Blog(title='mytitle',is_active=True,language=Language.PYTHON)
# print(blog1)
# blog2=Blog(title='my second blog',is_active=True,language='java')
# print(blog2)
# time.sleep(3)
# blog3=Blog(title='my third blog',is_active=True)
# print(blog3)

# print("users")
# user1=User(login="barto1993",password="Polibuda!",is_active=True,is_admin=True)
# time.sleep(5)
# user2=User(login="kate24",password="kathly123",is_active=True,is_admin=False)
# users=[user1,user2]
# print([u.created_at for u in users])

# print("new blog class")

# class Blog(BaseModel):
#     title:str=Field(min_length=10)
#     description:Optional[str]=None
#     is_active:bool
#     language:Language=Language.PYTHON
#     created_at:datetime=Field(default_factory=datetime.now)