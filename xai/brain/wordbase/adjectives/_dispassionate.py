

#calss header
class _DISPASSIONATE():
	def __init__(self,): 
		self.name = "DISPASSIONATE"
		self.definitions = [u'able to think clearly or make good decisions because of not being influenced by emotions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
