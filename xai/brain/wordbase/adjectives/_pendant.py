

#calss header
class _PENDANT():
	def __init__(self,): 
		self.name = "PENDANT"
		self.definitions = [u'\u2192\xa0 pendent ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
