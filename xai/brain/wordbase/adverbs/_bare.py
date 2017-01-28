

#calss header
class _BARE():
	def __init__(self,): 
		self.name = "BARE"
		self.definitions = [u'very: ', u'a lot; very much: ', u'a large number or amount of; a lot of: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
