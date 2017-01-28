

#calss header
class _STOCKY():
	def __init__(self,): 
		self.name = "STOCKY"
		self.definitions = [u'A stocky person, especially a man is fairly short and has a body that is wide across the shoulders and chest: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
