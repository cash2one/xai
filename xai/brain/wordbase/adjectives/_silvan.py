

#calss header
class _SILVAN():
	def __init__(self,): 
		self.name = "SILVAN"
		self.definitions = [u'of or having woods']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
