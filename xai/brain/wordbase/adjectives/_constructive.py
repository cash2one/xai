

#calss header
class _CONSTRUCTIVE():
	def __init__(self,): 
		self.name = "CONSTRUCTIVE"
		self.definitions = [u'If advice, criticism, or actions are constructive, they are useful and intended to help or improve something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
