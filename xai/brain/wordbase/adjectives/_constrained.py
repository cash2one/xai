

#calss header
class _CONSTRAINED():
	def __init__(self,): 
		self.name = "CONSTRAINED"
		self.definitions = [u'forced to do something against your will: ', u'Constrained behaviour is forced and unnatural: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
