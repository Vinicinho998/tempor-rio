from sells.calc_precos import  increase, decrease
from sells.format.price import real


aumenta = increase(100, 10, formatar=True)
diminui = decrease(100, 10)

print(aumenta)
print(diminui)

print(real(120))