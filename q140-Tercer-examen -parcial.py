# Control de los jugadores en cada categoría, las categorías se conforman de acuerdo con la edad y pueden tener varios jugadores.

class Jugador:
    def __init__(self, nombre, ano_nac, sexo, becado):
        self.nombre = nombre
        self.ano_nac = ano_nac
        self.sexo = sexo
        self.becado = becado

    def __str__(self):
        becado_str = "Becado" if self.becado else "Sin Beca"
        return f'Nombre: {self.nombre:<20} AñoNac: {self.ano_nac:<4} Sexo: {self.sexo:<5} Becado: {becado_str}'

class Categoria:
    def __init__(self, nombre, rango, costo):
        self.nombre = nombre
        self.rango = rango
        self.costo = costo
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def subtotal_categoria(self):
        subtotal = 0
        for jugador in self.jugadores:
            if not jugador.becado:
                subtotal += self.costo
        return subtotal

    def __str__(self):
        return f'Nombre: {self.nombre:<10} Rango: {self.rango:<15} Costo: ${self.costo:,.2f}'

class Academia:
    def __init__(self, nombre, propietario, domicilio):
        self.nombre = nombre
        self.propietario = propietario
        self.domicilio = domicilio
        self.categorias = []

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)

    def total_hombres(self):
        total = 0
        for categoria in self.categorias:
            for jugador in categoria.jugadores:
                if jugador.sexo == 'Hombre':
                    total += 1
        return total

    def total_mujeres(self):
        total = 0
        for categoria in self.categorias:
            for jugador in categoria.jugadores:
                if jugador.sexo == 'Mujer':
                    total += 1
        return total

    def total_ingresos(self):
        total = 0
        for categoria in self.categorias:
            total += categoria.subtotal_categoria()
        return total

    def __str__(self):
        return f'Nombre: {self.nombre} Propietario: {self.propietario} Domicilio: {self.domicilio}'


def imprimir_reporte(academia):
    print("REPORTE DEL CLUB DEPORTIVO")
    print(f'Nombre: {academia.nombre}')
    print(f'Propietario: {academia.propietario}')
    print(f'Domicilio: {academia.domicilio}')
    print(f'Total de Categorias: {len(academia.categorias)}')
    print(f'Total de Hombres: {academia.total_hombres()}')
    print(f'Total de Mujeres: {academia.total_mujeres()}')
    
    print(">> Datos generales de las Categorías")
    for categoria in academia.categorias:
        print(categoria)
    
    print(">> Jugadores por Categoría:")
    for categoria in academia.categorias:
        print(f'> {categoria.nombre} - {categoria.rango} - ({len(categoria.jugadores)})')
        subtotal_categoria = 0
        for jugador in categoria.jugadores:
            print(jugador)
            if not jugador.becado:
                subtotal_categoria += categoria.costo
        print(f'- SubTotal : ${subtotal_categoria:,.2f}')
    
    print(f'-> Total : ${academia.total_ingresos():,.2f}')

def main():
    
    academia = Academia("Academia Santos Laguna", "Francisco Nava", "Aguanaval 123, Hidráulica")

    
    categoria_1 = Categoria("Junior A", "2006/2007/2008", 1250)
    categoria_2 = Categoria("Junior B", "2009/2010/2011", 850)
    categoria_3 = Categoria("Pony A", "2012/2013/2014", 700)

    
    categoria_1.agregar_jugador(Jugador("Alexander Lopez", 2006, "Hombre", False))
    categoria_1.agregar_jugador(Jugador("Uriel Puga", 2007, "Hombre", True))
    categoria_1.agregar_jugador(Jugador("Alejandra Escalona", 2008, "Mujer", False))

    categoria_2.agregar_jugador(Jugador("Armando Santana", 2009, "Hombre", False))
    categoria_2.agregar_jugador(Jugador("Daniel Mijares", 2010, "Hombre", False))
    categoria_2.agregar_jugador(Jugador("Antonio Hernandez", 2011, "Mujer", True))

    categoria_3.agregar_jugador(Jugador("Andrea Solis", 2012, "Mujer", True))
    categoria_3.agregar_jugador(Jugador("Marissa Hernandez", 2013, "Mujer", True))
    categoria_3.agregar_jugador(Jugador("Diana Soto", 2014, "Mujer", False))


    academia.agregar_categoria(categoria_1)
    academia.agregar_categoria(categoria_2)
    academia.agregar_categoria(categoria_3)

    imprimir_reporte(academia)

if __name__ == "__main__":
    main()