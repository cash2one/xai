

#calss header
class _BABYISH():
	def __init__(self,): 
		self.name = "BABYISH"
		self.definitions = [u'only suitable for a baby: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
