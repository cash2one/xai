

#calss header
class _NEIGHBOURING():
	def __init__(self,): 
		self.name = "NEIGHBOURING"
		self.definitions = [u'Neighbouring places are next to or near each other: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
