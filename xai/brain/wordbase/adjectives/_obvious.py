

#calss header
class _OBVIOUS():
	def __init__(self,): 
		self.name = "OBVIOUS"
		self.definitions = [u'easy to see, recognize, or understand: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
