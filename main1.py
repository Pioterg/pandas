import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
# print(ts)
# ts.plot()
# plt.show()

# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
#         'Populacja': [11190846, 1303171035, 207847528, 38675467]}
# df = pd.DataFrame(data)
# print(df)
# grupa = df.groupby(['Kontynent']).agg({'Populacja':['sum']})
# print(grupa)
# wykres = grupa.plot.bar()
# wykres.set_ylabel('Mld')
# wykres.set_xlabel('Kontynent')
# wykres.tick_params(axis='x', labelrotation=0)
# wykres.legend()
# wykres.set_title('Populacja z podzialem na kontynenty')
# plt.savefig('wykres.png')
# plt.show()

# df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df)
# grupa = df.groupby(['Imię i nazwisko']).agg({'Wartość zamówienia':[sum]})
# grupa.plot(kind='pie', subplots=True, autopct='%.2f%%', fontsize=(6, 6), colors=['red', 'green'])
# plt.legend(loc='lower right')
# plt.title('Suma zamowienia dla sprzedawcy')
# plt.show()

# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
# df = pd.DataFrame(ts, columns=['Wartości'])
# print(df)
# df['Średnia krocząca'] = df.rolling(window=50).mean()
# df.plot()
# plt.legend()
# plt.show()

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)

#zad1
roczniki = df['Rok'].unique()
grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
wykres = grupa.plot()
wykres.set_ylabel('Liczba urodzonych dzieci')
wykres.set_xticks(roczniki)
wykres.tick_params(axis='x', labelrotation=40)
wykres.legend()
plt.subplots_adjust(left=0.15, right=0.9, bottom=0.15, top=0.9)
plt.title("Liczba urodzonych dzieci dla każdego roku")
plt.show()

#zad2
grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
wykres = grupa.plot.bar(ylabel='Liczba urodzeń')
wykres.legend()
plt.xticks(rotation=0)
plt.title("Liczba urodzonych chłopców i dziewczynek")
plt.show()

#zad3
grupa = df[df['Rok'] > 2012].groupby(['Plec']).agg({'Liczba':['sum']})
wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20)
plt.legend()
plt.show()

#zad4
df = pd.read_csv('zamowienia.csv', delimiter=';')
policzone = df.groupby('Sprzedawca').size()
policzone.plot.bar()
plt.ylabel("liczba zamówień")
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.2, top=0.9)
plt.title('Ilość zamówień sprzedawców')
plt.show()