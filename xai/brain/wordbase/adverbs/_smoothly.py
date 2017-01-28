

#calss header
class _SMOOTHLY():
	def __init__(self,): 
		self.name = "SMOOTHLY"
		self.definitions = [u'easily and without interruption or difficulty: ', u'without any sudden movements or changes: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
