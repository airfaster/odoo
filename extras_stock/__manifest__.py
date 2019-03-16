{
    'name': 'Campos extras para inventario',
    'version': '1.0',
    'category': 'Warehouse',
    'website': 'https://airfaster.net',
    'description': """
Modificando el registro de los modelos en stock.
========================================

Este modulo nos permitira agregar  los campos extras que se requieran para el 
el manejo de los procesos en el modulko de stock
""",
    'depends': ['base', 'stock'],
    'data': ['views/extras_move.xml'],
    'demo': [],
    'installable': True,
    'auto_install': False
}
