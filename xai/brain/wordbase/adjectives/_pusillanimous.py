

#calss header
class _PUSILLANIMOUS():
	def __init__(self,): 
		self.name = "PUSILLANIMOUS"
		self.definitions = [u'weak and cowardly (= not brave); frightened of taking risks: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
