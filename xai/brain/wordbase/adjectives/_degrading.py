

#calss header
class _DEGRADING():
	def __init__(self,): 
		self.name = "DEGRADING"
		self.definitions = [u'causing people to feel that they have no value: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
