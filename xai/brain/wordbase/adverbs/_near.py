

#calss header
class _NEAR():
	def __init__(self,): 
		self.name = "NEAR"
		self.definitions = [u'not far away in distance: ', u'not far away in time: ', u'almost in a particular state, or condition: ', u'not close in distance, time, amount, or quality: ', u'almost: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
