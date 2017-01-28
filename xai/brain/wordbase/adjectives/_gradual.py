

#calss header
class _GRADUAL():
	def __init__(self,): 
		self.name = "GRADUAL"
		self.definitions = [u'happening or changing slowly over a long period of time or distance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
