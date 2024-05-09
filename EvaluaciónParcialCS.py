class CalculadoraSueldo:
    def __init__(self, nombre_trabajador, sueldo_basico, dias_falta, minutos_tardanza, horas_extras):
              
        self.nombre_trabajador = nombre_trabajador
        self.sueldo_basico = sueldo_basico
        self.dias_falta = dias_falta
        self.minutos_tardanza = minutos_tardanza
        self.horas_extras = horas_extras

    #Nuestra primera version de prueba donde realizamos el constructor de la clase CalculadoraSueldo

    def calcular_sueldo(self):
        
        # Cálculo de bonificaciones
        pago_horas_extras = 1.50 * self.horas_extras * self.sueldo_basico / 30 / 8
        movilidad = 1000
        bonificacion_suplementaria = 0.03 * self.sueldo_basico
        bonificaciones = movilidad + bonificacion_suplementaria + pago_horas_extras

        # Cálculo de descuentos
        remuneracion_computable = self.sueldo_basico + movilidad + bonificacion_suplementaria
        remuneracion_minima = self.sueldo_basico + bonificaciones
        descuento_faltas = remuneracion_computable / 30 * self.dias_falta
        descuento_tardanzas = remuneracion_computable / 30 / 8 / 60 * self.minutos_tardanza
        descuentos = descuento_faltas + descuento_tardanzas

        # Cálculo sueldo neto
        sueldo_neto = self.sueldo_basico + bonificaciones - descuentos

        return sueldo_neto
    
    #Nuestra segunda version de prueba donde realizamos el metodo de calcular_sueldo

    def imprimir_boleta_pago(self):
        
        #Método para imprimir la boleta de pago del trabajador.
    
        sueldo_neto = self.calcular_sueldo()
        print("Boleta de Pago")
        print("Nombre del Trabajador:", self.nombre_trabajador)
        print("Sueldo Neto a Pagar:", sueldo_neto)

    #Nuestra tercera version de prueba donde realizamos el metodo de imprimir_boleta_pago

def main():
    
    #Función principal del programa.
    
    # Ingreso de datos
    nombre_trabajador = input("Ingrese nombre del trabajador: ")
    sueldo_basico = float(input("Ingrese sueldo básico del trabajador: "))
    dias_falta = int(input("Ingrese cantidad de días de falta: "))
    minutos_tardanza = int(input("Ingrese cantidad de minutos de tardanza: "))
    horas_extras = int(input("Ingrese cantidad de horas extras trabajadas: "))

    # Crear instancia de la calculadora de sueldo
    calculadora_sueldo = CalculadoraSueldo(nombre_trabajador, sueldo_basico, dias_falta, minutos_tardanza, horas_extras)

    # Imprimir boleta de pago
    calculadora_sueldo.imprimir_boleta_pago()

#Nuestra cuarta version de prueba donde realizamos el metodo de main

if __name__ == "__main__":
    main()

#Nuestra quinta y ultima version de prueba donde ejecutamos el programa
