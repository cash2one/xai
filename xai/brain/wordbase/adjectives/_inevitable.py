

#calss header
class _INEVITABLE():
	def __init__(self,): 
		self.name = "INEVITABLE"
		self.definitions = [u'certain to happen and unable to be avoided or prevented: ', u'something that is certain to happen and cannot be prevented: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
