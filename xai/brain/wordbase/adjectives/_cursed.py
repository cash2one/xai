

#calss header
class _CURSED():
	def __init__(self,): 
		self.name = "CURSED"
		self.definitions = [u'used to describe something that is annoying to you in an angry way: ', u'experiencing problems and unhappiness: ', u'experiencing bad luck caused by a magic curse: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
