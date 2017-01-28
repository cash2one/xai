

#calss header
class _EVIDENT():
	def __init__(self,): 
		self.name = "EVIDENT"
		self.definitions = [u'easily seen or understood: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
