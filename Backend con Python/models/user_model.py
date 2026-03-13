from pydantic import BaseModel, EmailStr, Field, model_validator, ConfigDict
from typing import Optional


# 1.CREO LA BASE
class UserBase(BaseModel):

    model_config = ConfigDict(extra='ignore')

    id: Optional[str] = None
    person_type: Optional[str] = None
    full_name: Optional[str] = None
    document_type: Optional[str] = None
    document_number: Optional[str] = None 
    email: Optional[str] = None
    rol_id: Optional[str] = "client"
    disabled:Optional[bool] = False
    phone: Optional[str] = None
    address: Optional[str] = None
    company_name: Optional[str] = None

    @model_validator(mode='after')
    def validate_company_by_type(self):
        if self.person_type == "Natural":
            self.company_name = None
        return self
    
# 2. LUEGO LA QUE HEREDA
class UserPassword(UserBase):
    password: str = Field(..., exclude=True)

# Se define por separado para que todos los campos sean opcionales
class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    person_type: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    document_type: Optional[str] = None
    document_number: Optional[str] = None
    company_name: Optional[str] = None