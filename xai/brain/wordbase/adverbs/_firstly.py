

#calss header
class _FIRSTLY():
	def __init__(self,): 
		self.name = "FIRSTLY"
		self.definitions = [u'used to refer to the first thing in a list: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
