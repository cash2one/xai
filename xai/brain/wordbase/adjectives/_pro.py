

#calss header
class _PRO():
	def __init__(self,): 
		self.name = "PRO"
		self.definitions = [u'supporting or agreeing with something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
