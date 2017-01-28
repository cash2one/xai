

#calss header
class _RAMBUNCTIOUS():
	def __init__(self,): 
		self.name = "RAMBUNCTIOUS"
		self.definitions = [u'full of energy and difficult to control: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
