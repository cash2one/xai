

#calss header
class _RAGLAN():
	def __init__(self,): 
		self.name = "RAGLAN"
		self.definitions = [u'(of a sleeve) sewn in two straight lines out from the neck to a point under the arm: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
