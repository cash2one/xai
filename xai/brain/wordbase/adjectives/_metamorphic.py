

#calss header
class _METAMORPHIC():
	def __init__(self,): 
		self.name = "METAMORPHIC"
		self.definitions = [u'(of rock) changed into a new form and structure by very great heat and pressure: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
