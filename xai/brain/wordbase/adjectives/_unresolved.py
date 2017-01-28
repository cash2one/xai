

#calss header
class _UNRESOLVED():
	def __init__(self,): 
		self.name = "UNRESOLVED"
		self.definitions = [u'If a problem or difficulty is unresolved, it is not solved or ended: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
