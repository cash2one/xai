

#calss header
class _LOUDLY():
	def __init__(self,): 
		self.name = "LOUDLY"
		self.definitions = [u'making a lot of noise: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
