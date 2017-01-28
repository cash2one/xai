

#calss header
class _UNFRIENDLY():
	def __init__(self,): 
		self.name = "UNFRIENDLY"
		self.definitions = [u'showing dislike and no sympathy']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
