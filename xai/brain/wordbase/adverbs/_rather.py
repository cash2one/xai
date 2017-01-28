

#calss header
class _RATHER():
	def __init__(self,): 
		self.name = "RATHER"
		self.definitions = [u'quite; to a slight degree: ', u'more accurately; more exactly: ', u'used to express an opposite opinion: ', u'instead of; used especially when you prefer one thing to another: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
