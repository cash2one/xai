

#calss header
class _DUFF():
	def __init__(self,): 
		self.name = "DUFF"
		self.definitions = [u'bad, not useful, or not working: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
