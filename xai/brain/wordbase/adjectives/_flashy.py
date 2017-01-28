

#calss header
class _FLASHY():
	def __init__(self,): 
		self.name = "FLASHY"
		self.definitions = [u'looking too bright, big, and expensive in a way that is intended to get attention and admiration: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
