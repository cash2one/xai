

#calss header
class _JUMPY():
	def __init__(self,): 
		self.name = "JUMPY"
		self.definitions = [u'nervous and worried, especially because you are frightened or guilty: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
