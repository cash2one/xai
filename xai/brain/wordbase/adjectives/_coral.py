

#calss header
class _CORAL():
	def __init__(self,): 
		self.name = "CORAL"
		self.definitions = [u'having a colour between orange and pink: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
