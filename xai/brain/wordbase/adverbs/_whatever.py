

#calss header
class _WHATEVER():
	def __init__(self,): 
		self.name = "WHATEVER"
		self.definitions = [u'\u2192\xa0 whatsoever : ', u'something that is said to show no respect to someone who is asking you to agree with them or agree to do something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
