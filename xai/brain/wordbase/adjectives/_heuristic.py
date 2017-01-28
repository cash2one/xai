

#calss header
class _HEURISTIC():
	def __init__(self,): 
		self.name = "HEURISTIC"
		self.definitions = [u'(of a method of teaching) allowing students to learn by discovering things themselves and learning from their own experiences rather than by telling them things']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
