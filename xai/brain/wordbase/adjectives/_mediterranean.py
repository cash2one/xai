

#calss header
class _MEDITERRANEAN():
	def __init__(self,): 
		self.name = "MEDITERRANEAN"
		self.definitions = [u'relating to the Mediterranean Sea or the countries around it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
