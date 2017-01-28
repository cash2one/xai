

#calss header
class _IDEAL():
	def __init__(self,): 
		self.name = "IDEAL"
		self.definitions = [u'perfect, or the best possible: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
