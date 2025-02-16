#Modulo para la clase token

#clase token
class Token:
  def __init__(self,type:str,value:str,lineon:int):
    self.type=type
    self.value=value
    self.lineon=lineon 

  def __str__(self):
    return f'Token({self.type},"{self.value}")'
  
  def __repr__(self):
    return str(self)