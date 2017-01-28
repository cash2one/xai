

#calss header
class _HIDEOUSLY():
	def __init__(self,): 
		self.name = "HIDEOUSLY"
		self.definitions = [u'in an extremely ugly way: ', u'used to emphasize the great degree of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
