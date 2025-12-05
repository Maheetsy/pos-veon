from pydantic import BaseModel, Field

class DecreaseStockRequest(BaseModel):
    quantity: int = Field(..., gt=0, description="Cantidad a descontar del stock")

