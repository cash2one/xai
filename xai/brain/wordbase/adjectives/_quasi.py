

#calss header
class _QUASI():
	def __init__(self,): 
		self.name = "QUASI"
		self.definitions = [u'used to show that something is almost, but not completely, the thing described: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
