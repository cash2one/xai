

#calss header
class _SPECIOUS():
	def __init__(self,): 
		self.name = "SPECIOUS"
		self.definitions = [u'seeming to be right or true, but really wrong or false: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
