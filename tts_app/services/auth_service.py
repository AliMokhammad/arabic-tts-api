from sqlalchemy.orm import Session

from tts_app.models.user import User
from tts_app.schemas.user import SignUpDto, LogInDto

from tts_app.utils.authentication import *
from tts_app.utils import response_handler


async def signup_user(user: SignUpDto, db: Session):
    if db.query(User).filter(User.email == user.email).first():
        return response_handler.error(message="Email already exists")

    new_user = User(email=user.email,password=user.password,first_name=user.first_name,last_name=user.last_name )

    db.add(new_user)
    db.commit()
    db.close()
    login_new_user = LogInDto(email = user.email, password = user.password)
    return await login_user(login_new_user, db)
    # return response_handler.success(message="User signed up successfully")


async def login_user(user: LogInDto, db: Session):
    user_data = db.query(User).filter(User.email == user.email).first()
    if not user_data:
        return response_handler.error(message="Invalid email or password")
    
    if user_data.password != user.password:
        return response_handler.error(message="Invalid email or password")
    
    access_token = create_access_token(user_data)
    data = user_data.to_dict()
    del data['password']

    data['access_token'] = access_token

    return response_handler.success(message="User logged in successfully", data=data)
