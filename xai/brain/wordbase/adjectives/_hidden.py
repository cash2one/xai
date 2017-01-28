

#calss header
class _HIDDEN():
	def __init__(self,): 
		self.name = "HIDDEN"
		self.definitions = [u'not easy to find: ', u'that most people do not know about: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
