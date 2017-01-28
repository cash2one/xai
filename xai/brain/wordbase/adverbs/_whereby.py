

#calss header
class _WHEREBY():
	def __init__(self,): 
		self.name = "WHEREBY"
		self.definitions = [u'by which way or method: ', u'in which, or with which: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
