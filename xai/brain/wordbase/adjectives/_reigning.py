

#calss header
class _REIGNING():
	def __init__(self,): 
		self.name = "REIGNING"
		self.definitions = [u'being the most recent winner of a competition: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
