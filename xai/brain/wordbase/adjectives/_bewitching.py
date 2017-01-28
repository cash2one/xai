

#calss header
class _BEWITCHING():
	def __init__(self,): 
		self.name = "BEWITCHING"
		self.definitions = [u'so beautiful or attractive that you cannot think about anything else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
