

#calss header
class _SOUTHEASTWARD():
	def __init__(self,): 
		self.name = "SOUTHEASTWARD"
		self.definitions = [u'towards the southeast: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
