

#calss header
class _CONFUCIAN():
	def __init__(self,): 
		self.name = "CONFUCIAN"
		self.definitions = [u'based on or believing in the ideas of the Chinese philosopher Confucius: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
