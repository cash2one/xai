

#calss header
class _RUBBERY():
	def __init__(self,): 
		self.name = "RUBBERY"
		self.definitions = [u'feeling or bending like rubber: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
