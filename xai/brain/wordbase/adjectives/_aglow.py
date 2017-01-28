

#calss header
class _AGLOW():
	def __init__(self,): 
		self.name = "AGLOW"
		self.definitions = [u'shining with light and colour: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
