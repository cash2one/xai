

#calss header
class _SLEEPLESS():
	def __init__(self,): 
		self.name = "SLEEPLESS"
		self.definitions = [u'without any sleep: ', u'not able to sleep: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
