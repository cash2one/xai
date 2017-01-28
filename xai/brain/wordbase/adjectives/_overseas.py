

#calss header
class _OVERSEAS():
	def __init__(self,): 
		self.name = "OVERSEAS"
		self.definitions = [u'in, from, or to other countries: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
