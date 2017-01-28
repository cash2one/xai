

#calss header
class _PREVALENT():
	def __init__(self,): 
		self.name = "PREVALENT"
		self.definitions = [u'existing very commonly or happening often: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
