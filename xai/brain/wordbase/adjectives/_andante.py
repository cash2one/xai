

#calss header
class _ANDANTE():
	def __init__(self,): 
		self.name = "ANDANTE"
		self.definitions = [u'(played) quite slowly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
