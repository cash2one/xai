

#calss header
class _LAUGHABLE():
	def __init__(self,): 
		self.name = "LAUGHABLE"
		self.definitions = [u'silly and not deserving to be seriously considered: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
