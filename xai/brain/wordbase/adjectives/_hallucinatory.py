

#calss header
class _HALLUCINATORY():
	def __init__(self,): 
		self.name = "HALLUCINATORY"
		self.definitions = [u'relating to or causing hallucinations: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
