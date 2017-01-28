

#calss header
class _GRANNY():
	def __init__(self,): 
		self.name = "GRANNY"
		self.definitions = [u'used of something that you wear, to mean having a style like those worn by old women: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
