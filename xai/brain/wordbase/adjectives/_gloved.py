

#calss header
class _GLOVED():
	def __init__(self,): 
		self.name = "GLOVED"
		self.definitions = [u'having a glove or gloves on: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
