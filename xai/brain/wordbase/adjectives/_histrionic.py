

#calss header
class _HISTRIONIC():
	def __init__(self,): 
		self.name = "HISTRIONIC"
		self.definitions = [u'very emotional and energetic, but not sincere or without real meaning: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
