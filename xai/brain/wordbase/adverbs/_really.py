

#calss header
class _REALLY():
	def __init__(self,): 
		self.name = "REALLY"
		self.definitions = [u'in fact: ', u'used to say that something is certain: ', u'very or very much: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
