# -*- coding: utf-8 -*-
"""
 		*** Loader

 		Created: 			 03 Apr 2019
		Last up: 	 		 04 Apr 2019
"""
from datascience import *
import numpy as np
import unidecode
import math

class Product(object):
	"""docstring for ClassName"""


	def print(self):
		print(	self.name, '\n',
				self.x_type, '\n',
				self.family, '\n',
				self.subfamily, '\n',
				self.treatment, '\n',
				self.zone, '\n',
				self.pathology, '\n',
				self.level, '\n',
				self.sessions, '\n',
				self.time, '\n',
				self.price, '\n',
				self.price_vip, '\n',
				self.price_company, '\n',
				self.price_session, '\n',
				self.price_session_next, '\n',
				self.price_max, '\n',
			)
	

	def __init__(self, name, x_type, family, subfamily, treatment, zone, pathology, level, sessions, time, \
																price, price_vip, price_company, price_session, price_session_next, price_max):
		self.name = name
		
		self.x_type = x_type
		self.family = family
		self.subfamily = subfamily

		self.treatment = treatment
		self.zone = zone
		self.pathology = pathology
		self.level = level
		self.sessions = sessions
		self.time = time

		self.price = price
		self.price_vip = price_vip
		self.price_company = price_company
		self.price_session = price_session
		self.price_session_next = price_session_next
		self.price_max = price_max


		# Validation
		self.x_type_arr = [	
							'service',
							'product',
			]

		self.family_arr = [	
							# Test
							'test',
							
							# Products
							'topical',

							# Service
							'laser',
							'ecography',
							'gynecology',
							'promotion',
							'medical',
							'cosmetology',
			]

		self.subfamily_arr = [	
								# Test 
								'test',

								# Products
								'chavarri',
								'commercial',

								# Laser
								'co2',
								'quick',
								'excilite',
								'm22',

								# Other
								'ecography',
								'gynecology',
								'promotion',
								'medical',
								'cosmetology',
			]


		self.treatment_arr = [	
								# Test
								'test_treatment',
								
								# Laser
								'LASER CO2 FRACCIONAL',
								'QUICKLASER',
								'LASER EXCILITE',
								'LASER M22 IPL',
								'LASER M22 ND YAG',
			
			]


		self.zone_arr = [	
								# Test
								'test_zone',

								# Co2
								'Todo Rostro',
								'Pomulos',
								'Cuello',
								'Manos',
								'Localizado Rostro',
								'Localizado Cuerpo',

								# Exc
								'Rostro',
								'Ariolas',
								'Axilas',
								'Pecho',
								'Abdomen',
								'Brazos',
								'Espalda',
								'Gluteos',
								'Hombros',
								'Manos',
								'Piernas',
								'Pies',

			]


		self.pathology_arr = [
								# Test
								'test_pathology',

								# Co2
								'Rejuvenecimiento',
								'Acne y Secuelas',
								'Manchas',
								'Acne y Secuelas',
								'Rejuvenecimiento',
								'Queratosis',
								'Lunar',
								'Quiste',
								'Verruga',
								'Cicatriz',

								# Quick
								'Lunares Congenitos',
								'Tatuaje',

								# Exc
								'Vitiligo',
								'Psoriasis',
								'Vitiligo',
								'Alopecias',

								# M22
								'Rosacea',
								'Varices',
								'Telangectacias',
								'Puntos Rubi',
								'Hemangiomas',
								'Acne Activo',
								'Rejuvenecimiento',
								'Depilacion',
			]


		self.level_arr = [	
								# Test
								'test_level',

								'Grado 1',
								'Grado 2',
								'Grado 3',
								'Grado 4',
								'Grado 5',

								# Empty
								'-1',
								-1,
			]

		self.sessions_arr = [	
								# Test
								'test_session',
								
								'1 sesion',
								'5 sesiones',
								'6 sesiones',
			]


		self.time_arr = [	
								# Test
								'test_time',
								
								'2 min',
								'5 min',
								'15 min',
								'30 min',

								'-1',
								-1,
			]



	def validate(self):
		"""
	 	Data Validation
	 		Type
	 		Family
	 		Subfamily
	 		Treatment
	 		Zone
	 		Pathology
	 		Level
	 		Sessions
	 		Time

	 		Price
		"""

		if self.x_type not in self.x_type_arr:
			print('Validation Error: Type')

		if self.family not in self.family_arr:
			print('Validation Error: Family')

		if self.subfamily not in self.subfamily_arr:
			print('Validation Error: Subfamily')

		if self.treatment not in self.treatment_arr:
			print('Validation Error: Treatment')

		if self.zone not in self.zone_arr:
			print('Validation Error: Zone - ', self.zone)

		if self.pathology not in self.pathology_arr:
			print('Validation Error: Pathology - ', self.pathology)

		if self.level not in self.level_arr:
			print('Validation Error: Level - ', self.level)
			
		if self.sessions not in self.sessions_arr:
			print('Validation Error: Sessions - ', self.sessions)

		if self.time not in self.time_arr:
			print('Validation Error: Time - ', self.time)



class Loader:
	"""
	Loads data from CSV, created by Excel. 
	Validates for categories. 
	"""

	def __init__(self):
		print('init')
		self.data = './csv/'


	def test(self):
		"""
		Tests the following families:
		Test
		Co2
		Quick
		Excilite
		M22
		"""
		print('test')		

		sub_arr = [
					'tst',
					'co2',
					'qui',
					'exc',
					'm22',
		]

		
		for sub in sub_arr:
			print(sub)
			self.create(sub)



	def create(self, name):
		"""
		Create Product object, from Table
		"""
		
		obj = self.dic[name]

		for row in obj.rows:
			
			#print(row.idx, row.name)
			
			name = row.name
			x_type = row.x_type
			family = row.family
			subfamily = row.subfamily
			
			treatment = row.treatment


			#unaccented_string = unidecode.unidecode(accented_string)

			#zone = row.zone
			zone = unidecode.unidecode(row.zone)

			#pathology = row.pathology
			pathology = unidecode.unidecode(row.pathology)
			


			#if level in ['nan', ' nan ']:
			#	level = ''

			#if level in [False]:
			#	print('Gotcha !')

			#x = float('nan')
			#x = float(level)
			#math.isnan(x)
			
			

			level = row.level
			

			#if math.isnan(row.level):
				#print('Gotcha !')
			#	level = ''
			#else:
			#	level = row.level


			#if isinstance(row.level, str):
			#	level = row.level

			#elif math.isnan(row.level):
				#print('Gotcha !')
			#	level = ''



			#print('.',level,'.')

			sessions = row.sessions
			
			time = row.time

			price = row.price
			price_vip = row.price_vip
			price_company = row.price_company
			price_session = row.price_session
			price_session_next = row.price_session_next
			price_max = row.price_max


			# Create 
			product = Product(name, x_type, family, subfamily, treatment, zone, pathology, level, sessions, time, \
																price, price_vip, price_company, price_session, price_session_next, price_max)

			#product.print()

			product.validate()



	def write(self):
		"""
	 	Write to CSV
		"""
		name = 'services.csv'
		#self.tst.to_csv(name)	
		self.co2.to_csv(name)			


	def read(self):
		"""
		Reads from CSV, created by Excel
		Creates Tables, using the DataScience lib
		"""
		print('read')


		# Read
		#data = './csv/'

		self.tst = Table.read_table(self.data + 'TEST.csv')

		self.co2 = Table.read_table(self.data + 'CO2.csv')
		self.qui = Table.read_table(self.data + 'QUICK.csv')
		self.exc = Table.read_table(self.data + 'EXCILITE.csv')
		self.m22 = Table.read_table(self.data + 'M22.csv')
		self.cos = Table.read_table(self.data + 'COSMETO.csv')
		self.med = Table.read_table(self.data + 'MEDICAL.csv')
		self.gyn = Table.read_table(self.data + 'GINECO.csv')
		self.eco = Table.read_table(self.data + 'ECO.csv')
		self.pro = Table.read_table(self.data +'PROMOS.csv')


		# Objs
		self.prods = Table.read_table(self.data + 'PRODUCTS.csv')

		self.servs = self.co2
		self.servs.append(self.qui)
		self.servs.append(self.exc)
		self.servs.append(self.m22)
		
		self.servs.append(self.cos)
		self.servs.append(self.med)
		self.servs.append(self.gyn)
		self.servs.append(self.pro)
		self.servs.append(self.eco)

		self.co2 = Table.read_table(self.data + 'CO2.csv')

		# Groups
		self.sub = self.servs.group('subfamily').sort('count', descending=True)
		self.fam = self.servs.group('family').sort('count', descending=True)


		# Dic
		self.dic = {
					'tst':	self.tst,

					'co2':	self.co2,
					'qui':	self.qui,
					'exc':	self.exc,
					'm22':	self.m22,

					'cos':	self.cos,
					'med':	self.med,
					'gyn':	self.gyn,
					'pro':	self.pro,
					'eco':	self.eco,

					'prods':	self.prods,
		}



	def inspect(self, name):
		"""
		Inspect Tables, row by row
		"""
		print('inspect')


		obj = self.dic[name]

		#for row in self.servs.rows:
		#for row in self.co2.rows:
		#for row in self.qui.rows:
		for row in obj.rows:
			print(row.idx, row.name)



# Script
# --------

l = Loader()

l.read()

#l.inspect('co2')

#l.create('co2')

l.test()

#l.write()


# EOF