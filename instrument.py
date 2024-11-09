from dataclasses import dataclass

@dataclass
class Instrument:
    mark: str
    model: str
    price: float
    strings_count: int


class Baixo(Instrument):
    def tocar_baixo(self):
        return "Tocando bem baixo"  # Eu n sei oq colocar kkkkkkkk


class Violao(Instrument):
    def tocar_chitaozin_e_chororo(self):
        return "Tocando evidências"
    
    def tocar_bruno_e_marrone(self):
        return "Tocando um Sertanejo Gostoso"
    
    def tocar_paula_fernandes(self):
        return "Tocando Pássaro de Fogo"


class Guitarra(Instrument):
    def tocar_guns_n_roses(self):
        return "Tocando Guns N' Roses"

    def tocar_guitar_hero(self):
        return "Tocando um Guitar Hero maneiro"
