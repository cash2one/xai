

#calss header
class _CLOTHED():
	def __init__(self,): 
		self.name = "CLOTHED"
		self.definitions = [u'wearing clothes: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
