

#calss header
class _BLANKLY():
	def __init__(self,): 
		self.name = "BLANKLY"
		self.definitions = [u'in a way that shows no understanding, interest, or emotion: ', u'completely or absolutely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
