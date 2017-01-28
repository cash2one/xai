

#calss header
class _MOLDY():
	def __init__(self,): 
		self.name = "MOLDY"
		self.definitions = [u'US spelling of  mouldy ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
