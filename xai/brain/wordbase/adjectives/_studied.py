

#calss header
class _STUDIED():
	def __init__(self,): 
		self.name = "STUDIED"
		self.definitions = [u'very carefully and intentionally done, made, or considered, rather than in a completely honest or sincere way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
