from pydantic import BaseModel, Field


class DetalhesImagemModelo(BaseModel):
    titulo: str = Field(description="Defina o titulo adequado para a imagem que for analisada.")
    descrisao: str = Field(description="Coloque aqui uma descrição detalha de sua análise para imagem.")
    rotulos: list[str] = Field(description="Defina  três rótulos principais para a imagem analisada.")
