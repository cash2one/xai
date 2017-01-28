

#calss header
class _MAYBE():
	def __init__(self,): 
		self.name = "MAYBE"
		self.definitions = [u'used to show that something is possible or that something might be true: ', u'used to show that a number or amount is approximate: ', u'used to politely suggest or ask for something: ', u'used to avoid giving a clear or certain answer to a question: ', u'used to mean that something is a possible explanation for why something else happened: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
