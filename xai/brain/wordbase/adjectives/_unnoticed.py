

#calss header
class _UNNOTICED():
	def __init__(self,): 
		self.name = "UNNOTICED"
		self.definitions = [u'without being seen or noticed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
