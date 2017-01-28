

#calss header
class _UNENDING():
	def __init__(self,): 
		self.name = "UNENDING"
		self.definitions = [u'used to describe activities or events, especially unpleasant ones, when they seem to continue for ever: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
