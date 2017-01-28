

#calss header
class _OTHERWISE():
	def __init__(self,): 
		self.name = "OTHERWISE"
		self.definitions = [u'differently, or in another way: ', u'except for what has just been referred to: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
