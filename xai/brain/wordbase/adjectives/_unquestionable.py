

#calss header
class _UNQUESTIONABLE():
	def __init__(self,): 
		self.name = "UNQUESTIONABLE"
		self.definitions = [u'obvious and impossible to doubt']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
