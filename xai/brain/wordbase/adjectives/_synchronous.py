

#calss header
class _SYNCHRONOUS():
	def __init__(self,): 
		self.name = "SYNCHRONOUS"
		self.definitions = [u'happening or done at the same time or speed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
