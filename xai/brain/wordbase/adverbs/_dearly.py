

#calss header
class _DEARLY():
	def __init__(self,): 
		self.name = "DEARLY"
		self.definitions = [u'very much: ', u'in a way that is expensive: ', u'to suffer a lot as a result of a particular action or event: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
