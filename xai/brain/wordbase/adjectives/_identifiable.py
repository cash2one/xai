

#calss header
class _IDENTIFIABLE():
	def __init__(self,): 
		self.name = "IDENTIFIABLE"
		self.definitions = [u'able to be recognized: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
