

#calss header
class _WOOZY():
	def __init__(self,): 
		self.name = "WOOZY"
		self.definitions = [u'feeling weak or ill and unable to think clearly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
