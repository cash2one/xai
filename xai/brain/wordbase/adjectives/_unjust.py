

#calss header
class _UNJUST():
	def __init__(self,): 
		self.name = "UNJUST"
		self.definitions = [u'not fair: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
