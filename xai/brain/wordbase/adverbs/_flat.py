

#calss header
class _FLAT():
	def __init__(self,): 
		self.name = "FLAT"
		self.definitions = [u'in a level position, often against another surface: ', u'into a flat shape without height: ', u'completely or to the greatest degree possible: ', u'exactly three minutes, half an hour, etc.: ', u'as fast or as hard as possible: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
