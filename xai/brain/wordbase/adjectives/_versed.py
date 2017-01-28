

#calss header
class _VERSED():
	def __init__(self,): 
		self.name = "VERSED"
		self.definitions = [u'to know a lot about a particular subject or be experienced in a particular skill: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
