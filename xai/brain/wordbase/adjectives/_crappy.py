

#calss header
class _CRAPPY():
	def __init__(self,): 
		self.name = "CRAPPY"
		self.definitions = [u'unpleasant or of very bad quality: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
