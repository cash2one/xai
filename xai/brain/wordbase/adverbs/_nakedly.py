

#calss header
class _NAKEDLY():
	def __init__(self,): 
		self.name = "NAKEDLY"
		self.definitions = [u'in a way that is obvious and unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
