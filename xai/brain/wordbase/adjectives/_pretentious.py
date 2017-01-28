

#calss header
class _PRETENTIOUS():
	def __init__(self,): 
		self.name = "PRETENTIOUS"
		self.definitions = [u'trying to appear or sound more important or clever than you are, especially in matters of art and literature: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
