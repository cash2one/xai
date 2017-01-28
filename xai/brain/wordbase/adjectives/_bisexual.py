

#calss header
class _BISEXUAL():
	def __init__(self,): 
		self.name = "BISEXUAL"
		self.definitions = [u'sexually attracted to both men and women: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
