

#calss header
class _DOPEY():
	def __init__(self,): 
		self.name = "DOPEY"
		self.definitions = [u'wanting to sleep, because or as if you have taken a drug: ', u'silly or stupid: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
