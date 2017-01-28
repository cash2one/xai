

#calss header
class _THORNY():
	def __init__(self,): 
		self.name = "THORNY"
		self.definitions = [u'A thorny problem or subject is difficult to deal with: ', u'having thorns: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
