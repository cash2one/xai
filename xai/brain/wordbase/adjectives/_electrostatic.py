

#calss header
class _ELECTROSTATIC():
	def __init__(self,): 
		self.name = "ELECTROSTATIC"
		self.definitions = [u'relating to or caused by electricity that does not move in a current but is attracted to the surface of some objects: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
