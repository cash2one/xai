

#calss header
class _RESPECTED():
	def __init__(self,): 
		self.name = "RESPECTED"
		self.definitions = [u'admired by many people for your qualities or achievements: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
