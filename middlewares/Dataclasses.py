from dataclasses import dataclass

@dataclass
class BotData:
    token:str
    admin:str

@dataclass
class DatabaseData:
    user:str
    password:str
    host:str
    port:int
    db:str