# Integrantes:
# Ambar Barrera
# Jesus Valencia
# Mayerly Reyes
# Matías Ron
# Cecilia Jacome

from pedido_mesa import PedidoMesa
from pedido_domicilio import PedidoDomicilio
from gestor_pedidos import GestorPedidos


pedido1 = PedidoMesa(
    "P001",
    "Carlos",
    25,
    5
)

pedido2 = PedidoDomicilio(
    "P002",
    "Ana",
    30,
    3
)

pedido3 = PedidoMesa(
    "P003",
    "Luis",
    40,
    6
)

lista_pedidos = [
    pedido1,
    pedido2,
    pedido3
]

# Crear una instancia del gestor
gestor = GestorPedidos()

print("INFORMACIÓN DE PEDIDOS")

# Llamamos al método desde su instancia
gestor.mostrar_pedidos(lista_pedidos)

print("\nTOTAL GENERAL EN DÓLARES")

# Llamar al método desde la instancia
print(
    gestor.calcular_total_pedidos(lista_pedidos)
)

print("\n USO DE STR")  

print(pedido1)
print(pedido2)
print(pedido3)