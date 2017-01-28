

#calss header
class _BADLY():
	def __init__(self,): 
		self.name = "BADLY"
		self.definitions = [u'in a severe and harmful way: ', u'in a way that is not acceptable or of good quality: ', u'very much: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
