

#calss header
class _DESIGNER():
	def __init__(self,): 
		self.name = "DESIGNER"
		self.definitions = [u'made by a famous or fashionable designer: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
