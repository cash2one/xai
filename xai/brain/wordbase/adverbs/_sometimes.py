

#calss header
class _SOMETIMES():
	def __init__(self,): 
		self.name = "SOMETIMES"
		self.definitions = [u'on some occasions but not always or often: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
