

#calss header
class _HALLUCINOGENIC():
	def __init__(self,): 
		self.name = "HALLUCINOGENIC"
		self.definitions = [u'causing hallucinations: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
