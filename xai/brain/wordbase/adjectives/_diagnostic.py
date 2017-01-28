

#calss header
class _DIAGNOSTIC():
	def __init__(self,): 
		self.name = "DIAGNOSTIC"
		self.definitions = [u'identifying a particular illness using a combination of signs and symptoms: ', u'used for making a judgment about what a particular problem is: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
