

#calss header
class _MIGHTILY():
	def __init__(self,): 
		self.name = "MIGHTILY"
		self.definitions = [u'with great effort: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
