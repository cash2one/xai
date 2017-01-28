

#calss header
class _APPARENTLY():
	def __init__(self,): 
		self.name = "APPARENTLY"
		self.definitions = [u'used to say you have read or been told something although you are not certain it is true: ', u'used when the real situation is different from what you thought it was: ', u'used to say that something seems to be true, although it is not certain: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
