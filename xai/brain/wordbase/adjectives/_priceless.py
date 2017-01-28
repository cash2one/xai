

#calss header
class _PRICELESS():
	def __init__(self,): 
		self.name = "PRICELESS"
		self.definitions = [u'A priceless object has such a high value, especially because it is rare, that the price of it cannot be calculated: ', u'extremely funny to see or hear: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
