

#calss header
class _HOPELESSLY():
	def __init__(self,): 
		self.name = "HOPELESSLY"
		self.definitions = [u'extremely, or in a way that makes you lose hope: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
