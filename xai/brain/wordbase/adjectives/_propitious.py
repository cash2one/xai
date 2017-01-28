

#calss header
class _PROPITIOUS():
	def __init__(self,): 
		self.name = "PROPITIOUS"
		self.definitions = [u'likely to result in success, or showing signs of success: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
