

#calss header
class _DEAD():
	def __init__(self,): 
		self.name = "DEAD"
		self.definitions = [u'complete(ly): ', u'very: ', u'to be completely opposed to something: ', u'to be very determined to do or have something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
