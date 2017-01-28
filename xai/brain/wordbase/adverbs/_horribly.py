

#calss header
class _HORRIBLY():
	def __init__(self,): 
		self.name = "HORRIBLY"
		self.definitions = [u'extremely, especially in a very bad or unpleasant way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
