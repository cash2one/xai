

#calss header
class _DECLARED():
	def __init__(self,): 
		self.name = "DECLARED"
		self.definitions = [u'A declared fact is one that someone has publicly said or admitted: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
