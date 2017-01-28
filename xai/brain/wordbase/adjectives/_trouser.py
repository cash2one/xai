

#calss header
class _TROUSER():
	def __init__(self,): 
		self.name = "TROUSER"
		self.definitions = [u'belonging or relating to trousers: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
