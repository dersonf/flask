from flask_table import Table, Col


class ItemTable(Table):
    '''Importa o título da table'''
    id = Col('ID')
    alimento = Col('Alimento')
    vegetal = Col('Vegetal')
