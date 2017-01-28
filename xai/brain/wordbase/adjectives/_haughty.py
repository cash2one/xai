

#calss header
class _HAUGHTY():
	def __init__(self,): 
		self.name = "HAUGHTY"
		self.definitions = [u'unfriendly and seeming to consider yourself better than other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
