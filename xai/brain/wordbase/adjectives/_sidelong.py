

#calss header
class _SIDELONG():
	def __init__(self,): 
		self.name = "SIDELONG"
		self.definitions = [u'used to refer to a short look at someone or something, moving your eyes to the side, and not looking directly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
