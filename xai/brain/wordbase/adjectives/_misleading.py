

#calss header
class _MISLEADING():
	def __init__(self,): 
		self.name = "MISLEADING"
		self.definitions = [u'causing someone to believe something that is not true: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
