

#calss header
class _ALTO():
	def __init__(self,): 
		self.name = "ALTO"
		self.definitions = [u'used to refer to a musical instrument that is of a size and range between soprano and tenor: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
