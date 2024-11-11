class VisualMain:
    def __init__(self):
        pass

    def showMenu(self):
        print("1) Compra")
        print("2) Venta")
        print("3) Reembolso")
        print("4) Inventario")
        print("5) Gestion Financiera")
        print("6) Gestion Clientes")
        print("7) Proyectos")
        print("8) RRHH")
        print("9) Reportes y analisis")
        print("10) Integraciones")
        print("11) Soporte y actualizaciones")
        print("12) Seguridad")
        print("13) Bot de asistencia")
        print("14) Plataforma de Eventos")
        print("x) Salir")
        return input("")
    
    def showError(self):
        print("Por favor elige una opcion valida.")