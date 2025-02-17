from prettytable import PrettyTable
from prettytable import TableStyle


table=PrettyTable() 
table.set_style(TableStyle.DOUBLE_BORDER)

table.field_names=['Pokemon Name','Type']
table.add_row(['Pikachu','Electric'])
table.add_row(['Squirtle','Water'])
table.add_divider()
table.add_row(['Charmander','Fire'])
table.add_row(['sm','Fire'],divider=True)
table.add_row(['fireyy','Water'])
table.add_column('Score',[25,47,45,57,78])
table.align='l'
# table.sortby='Score'
print(table)