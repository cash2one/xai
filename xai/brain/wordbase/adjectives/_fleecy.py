

#calss header
class _FLEECY():
	def __init__(self,): 
		self.name = "FLEECY"
		self.definitions = [u"soft and like a sheep's wool, or looking like this: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
