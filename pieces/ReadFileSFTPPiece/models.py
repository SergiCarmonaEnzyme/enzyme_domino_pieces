from pydantic import BaseModel, Field


class InputModel(BaseModel):
    
    host: str = Field(
        description="Server"
    )
    port: int = Field(
        description="Port"
    )
    user: str = Field(
        description="User"
    )
    password: str = Field(
        description="Password"
    )
    route: str = Field(
        description="Route"
    )
    file: str = Field(
        description="File"
    )

class OutputModel(BaseModel):
    """
    Sleep Piece Output Model
    """
    message: str = Field(
        description="Content File"
    )
