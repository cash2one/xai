

#calss header
class _BEARABLE():
	def __init__(self,): 
		self.name = "BEARABLE"
		self.definitions = [u'If an unpleasant situation is bearable, you can accept or deal with it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
