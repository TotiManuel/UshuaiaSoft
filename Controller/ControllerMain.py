#region Importaciones
#Primero importo librerias y luego los controladores
import os
from Visual.VisualMain import VisualMain
from Controller.ControllerCompra import ControllerCompra
from Controller.ControllerVenta import ControllerVenta
from Controller.ControllerReembolso import ControllerReembolso
from Controller.ControllerInventario import ControllerInventario
from Controller.ControllerGFinanciera import ControllerGFinanciera
from Controller.ControllerGClientes import ControllerGClientes
from Controller.ControllerProyectos import ControllerProyectos
from Controller.ControllerRRHH import ControllerRRHH
from Controller.ControllerReporteAnalisis import ControllerReporteAnalisis
from Controller.ControllerIntegraciones import ControllerIntegraciones
from Controller.ControllerSoporteActualizaciones import ControllerSoporteActualizaciones
from Controller.ControllerSeguridad import ControllerSeguridad
from Controller.ControllerBot import ControllerBot
from Controller.ControllerPEventos import ControllerPEventos
#endregion

class ControllerMain:
    def __init__(self):
        self.vista = VisualMain()
        self.controladorCompra = ControllerCompra()
        self.controladorVenta = ControllerVenta()
        self.controladorReembolso = ControllerReembolso()
        self.controladorInventario = ControllerInventario()
        self.controladorGFinanciera = ControllerGFinanciera()
        self.controladorGClientes = ControllerGClientes()
        self.controladorProyectos = ControllerProyectos()
        self.controladorRRHH = ControllerRRHH()
        self.controladorReporteAnalisis = ControllerReporteAnalisis()
        self.controladorIntegraciones = ControllerIntegraciones()
        self.controladorSoporteActualizaciones = ControllerSoporteActualizaciones()
        self.controladorSeguridad = ControllerSeguridad()
        self.controladorBot = ControllerBot()
        self.controladorPEventos = ControllerPEventos()

    def limpiar(self):
        os.system("cls")

    def showMenu(self):
        opcionMenu = ""
        while opcionMenu != "x":
            opcionMenu = self.vista.showMenu()
            try:
                opcionMenu = int(opcionMenu)
                if opcionMenu == 1:
                    self.limpiar()
                    self.controladorCompra.OK()
                elif opcionMenu == 2:
                    self.limpiar()
                    self.controladorVenta.OK()
                elif opcionMenu == 3:
                    self.limpiar()
                    self.controladorReembolso.OK()
                elif opcionMenu == 4:
                    self.limpiar()
                    self.controladorInventario.OK()
                elif opcionMenu == 5:
                    self.limpiar()
                    self.controladorGFinanciera.OK()
                elif opcionMenu == 6:
                    self.limpiar()
                    self.controladorGClientes.OK()
                elif opcionMenu == 7:
                    self.limpiar()
                    self.controladorProyectos.OK()
                elif opcionMenu == 8:
                    self.limpiar()
                    self.controladorRRHH.OK()
                elif opcionMenu == 9:
                    self.limpiar()
                    self.controladorReporteAnalisis.OK()
                elif opcionMenu == 10:
                    self.limpiar()
                    self.controladorIntegraciones.OK()
                elif opcionMenu == 11:
                    self.limpiar()
                    self.controladorSoporteActualizaciones.OK()
                elif opcionMenu == 12:
                    self.limpiar()
                    self.controladorSeguridad.OK()
                elif opcionMenu == 13:
                    self.limpiar()
                    self.controladorBot.OK()
                elif opcionMenu == 14:
                    self.limpiar()
                    self.controladorPEventos.OK()
                else:
                    self.limpiar()
                    self.vista.showError()
            except:
                if opcionMenu == "x":
                    break
                else:
                    self.vista.showError()
