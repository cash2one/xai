

#calss header
class _MANILA():
	def __init__(self,): 
		self.name = "MANILA"
		self.definitions = [u'made of strong brown paper: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
