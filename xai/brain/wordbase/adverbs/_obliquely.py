

#calss header
class _OBLIQUELY():
	def __init__(self,): 
		self.name = "OBLIQUELY"
		self.definitions = [u'said in a way that is not direct, so that the real meaning is not immediately clear: ', u'in a slanting or sloping manner']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
