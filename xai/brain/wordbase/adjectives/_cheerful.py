

#calss header
class _CHEERFUL():
	def __init__(self,): 
		self.name = "CHEERFUL"
		self.definitions = [u'happy and positive: ', u'used to describe a place or thing that is bright and pleasant and makes you feel positive and happy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
