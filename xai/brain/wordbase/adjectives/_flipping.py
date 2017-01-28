

#calss header
class _FLIPPING():
	def __init__(self,): 
		self.name = "FLIPPING"
		self.definitions = [u'used to emphasize what is being said, or to express anger: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
