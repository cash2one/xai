

#calss header
class _HURTFUL():
	def __init__(self,): 
		self.name = "HURTFUL"
		self.definitions = [u'causing emotional pain: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
