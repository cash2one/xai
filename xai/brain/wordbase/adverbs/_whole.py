

#calss header
class _WHOLE():
	def __init__(self,): 
		self.name = "WHOLE"
		self.definitions = [u'as a single object and not in pieces: ', u'completely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
