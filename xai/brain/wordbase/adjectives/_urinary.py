

#calss header
class _URINARY():
	def __init__(self,): 
		self.name = "URINARY"
		self.definitions = [u'relating to urine or to the parts of the body that produce and carry urine: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
