

#calss header
class _AFFECTIONATE():
	def __init__(self,): 
		self.name = "AFFECTIONATE"
		self.definitions = [u'showing feelings of liking or love: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
