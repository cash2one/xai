

#calss header
class _BARBARIC():
	def __init__(self,): 
		self.name = "BARBARIC"
		self.definitions = [u'extremely cruel and unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
