

#calss header
class _DECEASED():
	def __init__(self,): 
		self.name = "DECEASED"
		self.definitions = [u'dead: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
