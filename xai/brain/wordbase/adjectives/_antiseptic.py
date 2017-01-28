

#calss header
class _ANTISEPTIC():
	def __init__(self,): 
		self.name = "ANTISEPTIC"
		self.definitions = [u'completely free from infection: ', u'too clean and showing no imagination and character: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
