

#calss header
class _NEEDED():
	def __init__(self,): 
		self.name = "NEEDED"
		self.definitions = [u'necessary or wanted: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
