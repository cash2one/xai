

#calss header
class _WORRYING():
	def __init__(self,): 
		self.name = "WORRYING"
		self.definitions = [u'making you feel unhappy and frightened: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
