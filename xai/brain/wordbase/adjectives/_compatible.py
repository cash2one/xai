

#calss header
class _COMPATIBLE():
	def __init__(self,): 
		self.name = "COMPATIBLE"
		self.definitions = [u'able to exist, live together, or work successfully with something or someone else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
