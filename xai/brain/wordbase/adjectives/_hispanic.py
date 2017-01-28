

#calss header
class _HISPANIC():
	def __init__(self,): 
		self.name = "HISPANIC"
		self.definitions = [u'connected with Spain or Spanish-speaking countries, especially those countries in Latin America']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
