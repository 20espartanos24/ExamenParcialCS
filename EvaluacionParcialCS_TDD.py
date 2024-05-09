import unittest

class CalculadoraSueldo:
    def __init__(self, nombre_trabajador, sueldo_basico, dias_falta, minutos_tardanza, horas_extras):
        
        #Constructor de la clase CalculadoraSueldo.
        
        self.nombre_trabajador = nombre_trabajador
        self.sueldo_basico = sueldo_basico
        self.dias_falta = dias_falta
        self.minutos_tardanza = minutos_tardanza
        self.horas_extras = horas_extras
    

    def calcular_sueldo(self):
        
        #Método para calcular el sueldo neto del trabajador.

        bonificaciones = self.calcular_bonificaciones()
        descuentos = self.calcular_descuentos()
        sueldo_neto = self.sueldo_basico + bonificaciones - descuentos
        return sueldo_neto

    def calcular_bonificaciones(self):
        
        #Método para calcular las bonificaciones del trabajador.

        pago_horas_extras = 1.50 * self.horas_extras * self.sueldo_basico / 30 / 8
        movilidad = 1000
        bonificacion_suplementaria = 0.03 * self.sueldo_basico
        bonificaciones = movilidad + bonificacion_suplementaria + pago_horas_extras
        return bonificaciones

    def calcular_descuentos(self):
        
        #Método para calcular los descuentos por faltas y tardanzas del trabajador.

        remuneracion_computable = self.sueldo_basico + 1000 + 0.03 * self.sueldo_basico
        descuento_faltas = remuneracion_computable / 30 * self.dias_falta
        descuento_tardanzas = remuneracion_computable / 30 / 8 / 60 * self.minutos_tardanza
        descuentos = descuento_faltas + descuento_tardanzas
        return descuentos

class TestCalculadoraSueldo(unittest.TestCase):
    def test_calcular_descuentos(self):
        calculadora_sueldo = CalculadoraSueldo("Juan", 2000, 2, 30, 5)
        descuentos_esperados = 2 * (2000 + 1000 + 0.03 * 2000) / 30 + 30 * (2000 + 1000 + 0.03 * 2000) / 30 / 8 / 60
        descuentos_reales = calculadora_sueldo.calcular_descuentos()
        self.assertAlmostEqual(descuentos_reales, descuentos_esperados)

if __name__ == "__main__":
    unittest.main()