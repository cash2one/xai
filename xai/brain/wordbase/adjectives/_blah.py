

#calss header
class _BLAH():
	def __init__(self,): 
		self.name = "BLAH"
		self.definitions = [u'boring or ordinary: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
