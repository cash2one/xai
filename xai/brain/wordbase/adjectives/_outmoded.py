

#calss header
class _OUTMODED():
	def __init__(self,): 
		self.name = "OUTMODED"
		self.definitions = [u'no longer modern, useful, or necessary: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
