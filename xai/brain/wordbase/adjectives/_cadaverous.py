

#calss header
class _CADAVEROUS():
	def __init__(self,): 
		self.name = "CADAVEROUS"
		self.definitions = [u'looking pale, thin, and ill: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
