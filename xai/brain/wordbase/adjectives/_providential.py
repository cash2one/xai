

#calss header
class _PROVIDENTIAL():
	def __init__(self,): 
		self.name = "PROVIDENTIAL"
		self.definitions = [u'happening exactly when needed but without being planned: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
