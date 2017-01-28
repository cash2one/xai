

#calss header
class _INDISPUTABLE():
	def __init__(self,): 
		self.name = "INDISPUTABLE"
		self.definitions = [u'true, and impossible to doubt: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
