

#calss header
class _TERSE():
	def __init__(self,): 
		self.name = "TERSE"
		self.definitions = [u'using few words, sometimes in a way that seems rude or unfriendly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
