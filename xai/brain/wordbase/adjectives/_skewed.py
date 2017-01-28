

#calss header
class _SKEWED():
	def __init__(self,): 
		self.name = "SKEWED"
		self.definitions = [u'not accurate or exact: ', u'not straight: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
