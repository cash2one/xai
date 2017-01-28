

#calss header
class _WITTY():
	def __init__(self,): 
		self.name = "WITTY"
		self.definitions = [u'using words in a clever and funny way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
