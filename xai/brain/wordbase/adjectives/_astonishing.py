

#calss header
class _ASTONISHING():
	def __init__(self,): 
		self.name = "ASTONISHING"
		self.definitions = [u'very surprising: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
