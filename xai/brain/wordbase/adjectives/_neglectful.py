

#calss header
class _NEGLECTFUL():
	def __init__(self,): 
		self.name = "NEGLECTFUL"
		self.definitions = [u'not giving enough care and attention to something or someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
