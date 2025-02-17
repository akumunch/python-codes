from prettytable import PrettyTable
from prettytable import TableStyle

Funds_table=PrettyTable()
Funds_table.set_style(TableStyle.DOUBLE_BORDER)

Funds_table.field_names=['Fund','Alpha','Beta','Sharpe Ratio','Sortino','Expense ratio(%)','Exit Load Days','Exit load value(%)','Fund Size (cr)','Growth over past year|3Y|5Y(%)']
'''beta==> stock volatility'''

Funds_table.add_row(['JM(FC)',9.07,0.96,1.16,2.21,0.56,30,1,5254.65,'10.8|23.6|21.7']) #better fund manager than hdfc imo. lower expense ratio. very low exit load period. but 10.8% v/s 14.5% growth over the past year. Flexicap Fund Direct Plan Growth . Flexicap Direct Plan Growth.
Funds_table.add_row(['HDFC(FC)',7.52,0.88,1.18,2.34,0.8,355,1,65966.82,'14.5|22.8|22.8'])
Funds_table.add_row(['Parag(FC)',6.05,0.68,1.09,1.57,0.63,'365|730','2|1 (on 10%+ withdrawal)',89703.46,'15.4|18.9|24.1'],divider=True)

Funds_table.add_row(['Nippon(MC)',8.29,0.94,1.12,1.94,0.78,365,'1 (on 10%+ withdrawal)',37593.67,'8.6|22.9|21.8'])
Funds_table.add_row(['ICICI(MC)👎',5.34,0.91,0.98,2.02,0.99,365,1,13850.38,'9.2|19.5|20.0'],divider=True)

Funds_table.add_row(['Nippom(L)',5.46,0.96,0.97,2.00,0.71,7,1,35667.30,'8.1|19.4|18.8'])
Funds_table.add_row(['ICICI(L)',3.53,0.88,0.84,1.74,0.91,365,1,63296.96,'8.1|16.6|18.3'],divider=True)

Funds_table.add_row(['Motilal(M)',8.44,0.94,1.2,1.55,0.65,365,1,24488,'24.9|29.6|27.7'])
Funds_table.add_row(['HDFC(M)',5.18,0.88,1.22,1.98,0.79,365,1,73510.09,'8.5|24.8|25.2'],divider=True)

Funds_table.add_row(['Bandhan(S)',7.92,0.9,1.07,1.92,0.45,365,1,148698.21,'14.7|25.6|NA'])
Funds_table.add_row(['Invesco(S)',7.14,0.78,1.06,1.48,0.41,365,1,5904.85,'10.9|22.7|26.4'],divider=True)

Funds_table.align='c'
print(Funds_table)
