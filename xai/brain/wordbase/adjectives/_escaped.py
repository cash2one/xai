

#calss header
class _ESCAPED():
	def __init__(self,): 
		self.name = "ESCAPED"
		self.definitions = [u'having got free: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
