

#calss header
class _HARD():
	def __init__(self,): 
		self.name = "HARD"
		self.definitions = [u'with a lot of physical or mental effort: ', u'If it rains or snows hard, it rains or snows a lot: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
