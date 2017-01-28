

#calss header
class _UNDERHAND():
	def __init__(self,): 
		self.name = "UNDERHAND"
		self.definitions = [u'(done by) moving the arm below shoulder level: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
