

#calss header
class _BREATHTAKING():
	def __init__(self,): 
		self.name = "BREATHTAKING"
		self.definitions = [u'extremely exciting, beautiful, or surprising: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
