

#calss header
class _FORFEIT():
	def __init__(self,): 
		self.name = "FORFEIT"
		self.definitions = [u'taken away from someone as a punishment']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
