

#calss header
class _GLITZY():
	def __init__(self,): 
		self.name = "GLITZY"
		self.definitions = [u'having a fashionable appearance intended to attract attention: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
