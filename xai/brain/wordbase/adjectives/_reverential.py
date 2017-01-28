

#calss header
class _REVERENTIAL():
	def __init__(self,): 
		self.name = "REVERENTIAL"
		self.definitions = [u'caused by, or full of respect and admiration: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
