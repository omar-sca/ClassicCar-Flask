from datetime import date
from datetime import datetime
import calendar
import operator

def between(n, limite_inf, limite_sup):
    # Los limites se incluyen en el intervalo
    return limite_inf <= n <= limite_sup


class FechaMY():
    def __init__(self, stringFecha):
        mes, year = stringFecha.split('-')
        mes = int(mes)
        year = int(year)
        if between(mes, 1, 12) and (year > date.today().year or (year == date.today().year and mes > date.today().month)):
            self.__mes = mes
            self.__year = year
        else:
            self.__dia_hoy = date.today().day
            self.__mes = date.today().month
            self.__year = date.today().year

        self.__fecha = self.__strFecha()
        self.__fechaSig = self.__strFechaSig()
        self.__fechaAnt = self.__strFechaAnt()
        self.__desface1erdia = self.__desface_1er_dia()
        self.__nombreMes = self.__strNombreMes()
        self.__nroUltDiaDelMes = self.__numeroUltimoDiaDelMes()


    @property
    def nroUltDiaDelMes(self):
        return self.__nroUltDiaDelMes

    @property
    def nombreMes(self):
        return self.__nombreMes

    @property
    def desface1erdia(self):
        return self.__desface1erdia

    @property
    def fecha(self):
        return self.__fecha

    @property
    def fechaAnt(self):
        return self.__fechaAnt

    @property
    def fechaSig(self):
        return self.__fechaSig

    @property
    def dia_hoy(self):
        return self.__dia_hoy

    @property
    def mes(self):
        return self.__mes

    @property
    def year(self):
        return self.__year

    def __formatFecha(self, mes, year):
        return str(mes) + '-' + str(year)

    def __strFecha(self):
        return self.__formatFecha(self.mes, self.year)

    def __incr_decr(self, operacion):
        mes = operacion(self.mes, 1)
        if mes == 13:
            mes = 1
            year = self.year+1
        elif mes == 0:
            mes = 12
            year = self.year-1
        else:
            year = self.year
        return self.__formatFecha(mes, year)

    def __strFechaSig(self):
        return self.__incr_decr(operator.add)

    def __strFechaAnt(self):
        return self.__incr_decr(operator.sub)

    def __desface_1er_dia(self):
        return datetime(self.year, self.mes, 1).weekday()

    def __strNombreMes(self):
        meses=[
            "",
            "Enero",
            "Febrero",
            "Marzo",
            "Abril",
            "Mayo",
            "Junio",
            "Julio",
            "Agosto",
            "Septiembre",
            "Octubre",
            "Noviembre",
            "Diciembre"]
        return meses[self.mes]

    def __numeroUltimoDiaDelMes(self):
        return calendar.monthrange(self.year, self.mes)[1]

def fecha_actual():
    var = str(date.today().month) + '-' + str(date.today().year)
    print("===VAR===")
    print(var)
    print("===VAR===")
    return var
