

#calss header
class _FORGIVABLE():
	def __init__(self,): 
		self.name = "FORGIVABLE"
		self.definitions = [u'used to say that you can forgive something because you understand it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
