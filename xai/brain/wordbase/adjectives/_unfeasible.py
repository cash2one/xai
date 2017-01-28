

#calss header
class _UNFEASIBLE():
	def __init__(self,): 
		self.name = "UNFEASIBLE"
		self.definitions = [u'not feasible (= able to be done or achieved)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
