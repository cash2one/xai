

#calss header
class _SUPERNUMERARY():
	def __init__(self,): 
		self.name = "SUPERNUMERARY"
		self.definitions = [u'in addition to the number usually needed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
