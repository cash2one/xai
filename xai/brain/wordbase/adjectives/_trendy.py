

#calss header
class _TRENDY():
	def __init__(self,): 
		self.name = "TRENDY"
		self.definitions = [u'modern and influenced by the most recent fashions or ideas: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
