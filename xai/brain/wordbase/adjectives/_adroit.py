

#calss header
class _ADROIT():
	def __init__(self,): 
		self.name = "ADROIT"
		self.definitions = [u'very skilful and quick in the way you think or move: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
