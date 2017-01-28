

#calss header
class _WOMANLY():
	def __init__(self,): 
		self.name = "WOMANLY"
		self.definitions = [u'Womanly qualities, ideas, or physical features are ones that a woman is typically or traditionally thought to have: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
