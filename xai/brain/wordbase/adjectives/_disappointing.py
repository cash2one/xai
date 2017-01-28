

#calss header
class _DISAPPOINTING():
	def __init__(self,): 
		self.name = "DISAPPOINTING"
		self.definitions = [u'making you feel disappointed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
