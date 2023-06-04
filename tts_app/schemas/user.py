from pydantic import BaseModel, EmailStr, Field

class SignUpDto(BaseModel):
    password: str = Field(title="Password is required")
    email: EmailStr = Field(title="Email is not correct")
    first_name: str = Field(title="First Name is required")
    last_name: str = Field(title="Last Name is required")

class LogInDto(BaseModel):
    password: str = Field(title="Password is required")
    email: EmailStr = Field(title="Email is not correct")
