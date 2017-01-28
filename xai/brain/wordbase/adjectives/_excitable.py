

#calss header
class _EXCITABLE():
	def __init__(self,): 
		self.name = "EXCITABLE"
		self.definitions = [u'easily and often becoming excited: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
