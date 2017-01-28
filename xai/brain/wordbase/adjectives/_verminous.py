

#calss header
class _VERMINOUS():
	def __init__(self,): 
		self.name = "VERMINOUS"
		self.definitions = [u'covered with insects: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
