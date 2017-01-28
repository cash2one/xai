

#calss header
class _CLEARLY():
	def __init__(self,): 
		self.name = "CLEARLY"
		self.definitions = [u'in a way that is easy to see, hear, read, or understand', u'used to show that you think something is obvious or certain: ', u'When you think clearly, you are not confused.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
