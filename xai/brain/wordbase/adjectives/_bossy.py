

#calss header
class _BOSSY():
	def __init__(self,): 
		self.name = "BOSSY"
		self.definitions = [u'A bossy person is always telling people what to do.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
