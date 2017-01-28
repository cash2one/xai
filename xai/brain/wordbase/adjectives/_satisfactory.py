

#calss header
class _SATISFACTORY():
	def __init__(self,): 
		self.name = "SATISFACTORY"
		self.definitions = [u'good or good enough for a particular need or purpose: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
