

#calss header
class _STARK():
	def __init__(self,): 
		self.name = "STARK"
		self.definitions = [u'empty, simple, or obvious, especially without decoration or anything that is not necessary: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
