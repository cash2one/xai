

#calss header
class _MORTALLY():
	def __init__(self,): 
		self.name = "MORTALLY"
		self.definitions = [u'so severe that death is likely: ', u'extremely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
