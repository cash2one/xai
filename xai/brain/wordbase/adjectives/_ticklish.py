

#calss header
class _TICKLISH():
	def __init__(self,): 
		self.name = "TICKLISH"
		self.definitions = [u'If you are ticklish, you quickly feel uncomfortable when someone lightly touches your skin to make you laugh.', u'A ticklish situation is one that needs to be dealt with carefully: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
