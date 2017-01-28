

#calss header
class _BANDY():
	def __init__(self,): 
		self.name = "BANDY"
		self.definitions = [u'(of legs) bending out at the knees: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
