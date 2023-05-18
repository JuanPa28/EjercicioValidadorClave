from abc import ABC, abstractmethod
import re

from validadorclave.modelo.errores import NoCumpleLongitudMinimaError, NoTieneLetraMayusculaError, \
    NoTieneCaracterEspecialError, NoTieneLetraMinusculaError, NoTieneNumeroError, NoTienePalabraSecretaError


class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self.longitud_esperada = longitud_esperada

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass

    def _validar_longitud(self, clave: str) -> bool:
        if len(clave) < self.longitud_esperada:
            return False
        else:
            return True

    def _contiene_mayuscula(self, clave: str) -> bool:
        if any(caracter.isupper() for caracter in clave):
            return True
        else:
            return False

    def _contiene_minuscula(self, clave: str) -> bool:
        if any(caracter.islower() for caracter in clave):
            return True
        else:
            return False

    def _contiene_numero(self, clave: str) -> bool:
        if any(caracter.isdigit() for caracter in clave):
            return True
        else:
            return False

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass


class Validador():
    def __int__(self, regla: ReglaValidacion):
        self.regla = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave)


class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(8)

    def contiene_caracter_especial(clave: str) -> bool:
        if not any(c in '@ _ # $ %' for c in clave):
            raise NoTieneCaracterEspecialError("Se esperaba al menos un caracter especial...")
        return True

    def es_valida(self, clave: str) -> bool:
        if (not self._validar_longitud(clave)):
            raise NoCumpleLongitudMinimaError("Se esperaba al menos", self.longitud_esperada, "caracteres...")

        if (not self._contiene_mayuscula(clave)):
            raise NoTieneLetraMayusculaError("Se esperaba al menos una letra mayuscula...")

        if (not self._contiene_minuscula(clave)):
            raise NoTieneLetraMinusculaError("Se esperaba al menos una letra minuscula...")

        if (not self._contiene_numero(clave)):
            raise NoTieneNumeroError("Se esperaba al menos un numero...")

        return True
class ReglaValidacionCalisto(ReglaValidacion):

    def __init__(self):
        super().__init__(6)

    def contiene_calisto(clave: str) -> bool:
        if not clave.find('CalistO'):
            raise NoTienePalabraSecretaError ("Mo contiene la palabra secreta...")

    def es_valida(self, clave: str) -> bool:
        if (not self._contiene_numero(clave)):
            raise NoTieneLetraMayusculaError("Se esperaba al menos un numero...")