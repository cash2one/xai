

#calss header
class _UNTIMELY():
	def __init__(self,): 
		self.name = "UNTIMELY"
		self.definitions = [u'Something bad that is untimely happens unexpectedly early or at a time that is not suitable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
