

#calss header
class _WILFUL():
	def __init__(self,): 
		self.name = "WILFUL"
		self.definitions = [u'(of something bad) done intentionally or (of a person) determined to do exactly as you want, even if you know it is wrong: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
