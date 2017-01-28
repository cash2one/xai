

#calss header
class _UNFLAPPABLE():
	def __init__(self,): 
		self.name = "UNFLAPPABLE"
		self.definitions = [u'not likely to get worried, nervous, or angry even in difficult situations: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
