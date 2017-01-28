

#calss header
class _CANTANKEROUS():
	def __init__(self,): 
		self.name = "CANTANKEROUS"
		self.definitions = [u'arguing and complaining a lot: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
