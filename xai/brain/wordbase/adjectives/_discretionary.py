

#calss header
class _DISCRETIONARY():
	def __init__(self,): 
		self.name = "DISCRETIONARY"
		self.definitions = [u'decided by officials and not fixed by rules: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
