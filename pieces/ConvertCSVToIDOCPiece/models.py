from pydantic import BaseModel, Field


class InputModel(BaseModel):
    file_content: str = Field(
        description="Content File"
    )

class OutputModel(BaseModel):
    idoc_content: str = Field(
        description="File content in IDOC"
    )
