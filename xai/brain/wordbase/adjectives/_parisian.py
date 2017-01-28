

#calss header
class _PARISIAN():
	def __init__(self,): 
		self.name = "PARISIAN"
		self.definitions = [u'from, belonging to, or relating to the city of Paris in France: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
