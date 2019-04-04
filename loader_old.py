from datascience import *
import numpy as np



# Read
data = './csv/'
co2 = Table.read_table(data + 'CO2.csv')
qui = Table.read_table(data + 'QUICK.csv')
exc = Table.read_table(data + 'EXCILITE.csv')
m22 = Table.read_table(data + 'M22.csv')
cos = Table.read_table(data + 'COSMETO.csv')
med = Table.read_table(data + 'MEDICAL.csv')
gyn = Table.read_table(data + 'GINECO.csv')
eco = Table.read_table(data + 'ECO.csv')
pro = Table.read_table(data +'PROMOS.csv')
prods = Table.read_table(data + 'PRODUCTS.csv')


# Append

# Laser
servs = co2
servs.append(qui)
servs.append(exc)
servs.append(m22)

# Cosmeto
servs.append(cos)

# Medical
servs.append(med)

# Gyneco
servs.append(gyn)

# Promos
servs.append(pro)

# Eco
servs.append(eco)


# Groups
subs = servs.group('subfamily').sort('count', descending=True)
fams = servs.group('family').sort('count', descending=True)



