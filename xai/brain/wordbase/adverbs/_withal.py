

#calss header
class _WITHAL():
	def __init__(self,): 
		self.name = "WITHAL"
		self.definitions = [u'in addition: ', u'in spite of what has been said: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
