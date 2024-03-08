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
    idoc_content: str = Field(
        description="File content in IDOC"
    )
