

#calss header
class _MULTINATIONAL():
	def __init__(self,): 
		self.name = "MULTINATIONAL"
		self.definitions = [u'involving several different countries, or (of a business) producing and selling goods in several different countries: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
