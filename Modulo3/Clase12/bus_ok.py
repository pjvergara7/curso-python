class Transporte:
    def __init__(self) -> None:
        self.patentes = []
        self.movimientos = []
        self.tarifa = 730
        self.tarifario = {
            'adulto': self.tarifa,
            'niño': 0,
            'adulto_mayor': self.tarifa/2
        }

    def registar_patente(self, _patente, _chofer):
        patente = list(filter(lambda elemento: elemento['patente'] == _patente, self.patentes))

        if len(patente) > 0:
            print("La Patente ya se encuentra registrada")
        else:
            self.patentes.append({
                "patente": _patente,
                "chofer": _chofer
            })

    def cobrar_pasaje(self, _patente, _tipo_persona, _fecha):
        self.movimientos.append({
            "patente": _patente,
            "tipo_persona": _tipo_persona,
            "fecha": _fecha,
            "monto_cobrado": self.tarifario[_tipo_persona]
        })

    def reporte_diario(self, _tipo_reporte, _valor):
        movimientos = list(filter(lambda elemento: elemento[_tipo_reporte] == _valor, self.movimientos))
        total_cobrado = 0
        for pasaje in movimientos:
            total_cobrado += pasaje['monto_cobrado']
            print(pasaje['fecha'], pasaje['tipo_persona'], pasaje['monto_cobrado'])

        print("----------------")
        print(f'total cobrado es: {total_cobrado}')


empresa = Transporte()

empresa.registar_patente("xx-xx-xx", "Rodrigo")

empresa.cobrar_pasaje("xx-xx-xx", "adulto", "02-05-2023")
empresa.cobrar_pasaje("xx-xx-xx", "adulto_mayor", "02-05-2023")
empresa.cobrar_pasaje("xx-xx-xx", "adulto", "02-05-2023")


#empresa.reporte_diario("patente", "xx-xx-xx")
#empresa.reporte_diario("fecha", "02-05-2023")
empresa.reporte_diario("tipo_persona", "adulto_mayor")