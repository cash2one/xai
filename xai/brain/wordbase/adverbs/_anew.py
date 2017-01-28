

#calss header
class _ANEW():
	def __init__(self,): 
		self.name = "ANEW"
		self.definitions = [u'again or one more time, especially in a different way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
