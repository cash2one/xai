

#calss header
class _MOVABLE():
	def __init__(self,): 
		self.name = "MOVABLE"
		self.definitions = [u'able to be moved: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
