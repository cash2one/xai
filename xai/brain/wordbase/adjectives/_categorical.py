

#calss header
class _CATEGORICAL():
	def __init__(self,): 
		self.name = "CATEGORICAL"
		self.definitions = [u'without any doubt or possibility of being changed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
