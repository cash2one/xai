

#calss header
class _LUDICROUS():
	def __init__(self,): 
		self.name = "LUDICROUS"
		self.definitions = [u'stupid or unreasonable and deserving to be laughed at: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
