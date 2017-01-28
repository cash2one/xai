

#calss header
class _COMPELLED():
	def __init__(self,): 
		self.name = "COMPELLED"
		self.definitions = [u'having to do something, because you are forced to or feel it is necessary: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
