

#calss header
class _WOEFUL():
	def __init__(self,): 
		self.name = "WOEFUL"
		self.definitions = [u'very bad or (of something very bad or unpleasant) very large or extreme: ', u'extremely sad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
