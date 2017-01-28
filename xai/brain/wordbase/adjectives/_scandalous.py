

#calss header
class _SCANDALOUS():
	def __init__(self,): 
		self.name = "SCANDALOUS"
		self.definitions = [u'making people shocked and upset: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
