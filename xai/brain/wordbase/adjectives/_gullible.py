

#calss header
class _GULLIBLE():
	def __init__(self,): 
		self.name = "GULLIBLE"
		self.definitions = [u'easily deceived or tricked, and too willing to believe everything that other people say: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
