

#calss header
class _SEDATE():
	def __init__(self,): 
		self.name = "SEDATE"
		self.definitions = [u'avoiding excitement or great activity and usually calm and relaxed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
