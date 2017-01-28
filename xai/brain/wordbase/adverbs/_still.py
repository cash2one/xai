

#calss header
class _STILL():
	def __init__(self,): 
		self.name = "STILL"
		self.definitions = [u'continuing to happen or continuing to be done: ', u'despite that: ', u'to an even greater degree or in an even greater amount: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
