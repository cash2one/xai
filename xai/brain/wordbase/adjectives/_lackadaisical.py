

#calss header
class _LACKADAISICAL():
	def __init__(self,): 
		self.name = "LACKADAISICAL"
		self.definitions = [u'showing little enthusiasm and effort: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
