

#calss header
class _FAVORITE():
	def __init__(self,): 
		self.name = "FAVORITE"
		self.definitions = [u'US spelling of  favourite ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
