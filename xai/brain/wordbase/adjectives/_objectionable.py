

#calss header
class _OBJECTIONABLE():
	def __init__(self,): 
		self.name = "OBJECTIONABLE"
		self.definitions = [u'used to describe people or things that you dislike or oppose because they are so unpleasant or wrong: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
