

#calss header
class _MUTABLE():
	def __init__(self,): 
		self.name = "MUTABLE"
		self.definitions = [u'able or likely to change: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
