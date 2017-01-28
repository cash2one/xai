

#calss header
class _STRUCTURAL():
	def __init__(self,): 
		self.name = "STRUCTURAL"
		self.definitions = [u'relating to the way in which parts of a system or object are arranged: ', u'relating to the structure of a building or similar object: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
