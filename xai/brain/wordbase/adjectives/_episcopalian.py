

#calss header
class _EPISCOPALIAN():
	def __init__(self,): 
		self.name = "EPISCOPALIAN"
		self.definitions = [u'belonging or relating to the Episcopal Church']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
