

#calss header
class _PRETEND():
	def __init__(self,): 
		self.name = "PRETEND"
		self.definitions = [u'imaginary or not real: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
