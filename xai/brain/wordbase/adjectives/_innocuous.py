

#calss header
class _INNOCUOUS():
	def __init__(self,): 
		self.name = "INNOCUOUS"
		self.definitions = [u'completely harmless (= causing no harm): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
