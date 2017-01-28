

#calss header
class _HOMEWARD():
	def __init__(self,): 
		self.name = "HOMEWARD"
		self.definitions = [u'towards home: ', u'travelling towards home: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
