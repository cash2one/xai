

#calss header
class _IMMENSELY():
	def __init__(self,): 
		self.name = "IMMENSELY"
		self.definitions = [u'extremely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
