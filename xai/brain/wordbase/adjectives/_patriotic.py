

#calss header
class _PATRIOTIC():
	def __init__(self,): 
		self.name = "PATRIOTIC"
		self.definitions = [u'showing love for your country and being proud of it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
