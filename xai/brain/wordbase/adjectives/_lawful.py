

#calss header
class _LAWFUL():
	def __init__(self,): 
		self.name = "LAWFUL"
		self.definitions = [u'allowed by the law: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
