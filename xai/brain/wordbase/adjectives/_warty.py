

#calss header
class _WARTY():
	def __init__(self,): 
		self.name = "WARTY"
		self.definitions = [u'having warts']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
