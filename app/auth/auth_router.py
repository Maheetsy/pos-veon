from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from app.auth.jwt_handler import create_access_token, USERS_DB
from datetime import timedelta

router = APIRouter(prefix="/auth", tags=["Autenticación"])

class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    role: str

@router.post("/login", response_model=TokenResponse)
async def login(login_data: LoginRequest):
    """Endpoint para autenticación y obtención de token JWT"""
    user = USERS_DB.get(login_data.username)
    
    if not user or user["password"] != login_data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos"
        )
    
    access_token = create_access_token(
        data={"sub": user["user_id"], "role": user["role"]},
        expires_delta=timedelta(minutes=30)
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": user["role"]
    }

