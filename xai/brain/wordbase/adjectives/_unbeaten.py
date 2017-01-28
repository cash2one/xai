

#calss header
class _UNBEATEN():
	def __init__(self,): 
		self.name = "UNBEATEN"
		self.definitions = [u'in sports, having won every game: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
