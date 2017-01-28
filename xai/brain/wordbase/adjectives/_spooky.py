

#calss header
class _SPOOKY():
	def __init__(self,): 
		self.name = "SPOOKY"
		self.definitions = [u'strange and frightening: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
