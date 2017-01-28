

#calss header
class _MULTITUDINOUS():
	def __init__(self,): 
		self.name = "MULTITUDINOUS"
		self.definitions = [u'consisting of many things or parts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
