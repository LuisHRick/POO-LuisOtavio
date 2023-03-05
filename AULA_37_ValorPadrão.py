from dataclasses import dataclass, field


@dataclass()
class Pessoa:
    idade: int = 100
    nome: str = field(
        default='MISSING',  # Outras opções interessantes
    )
    sobrenome: str = 'Not Send'
    enderecos: list[str] = field(default_factory=list)
