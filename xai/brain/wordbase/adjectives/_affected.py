

#calss header
class _AFFECTED():
	def __init__(self,): 
		self.name = "AFFECTED"
		self.definitions = [u'artificial and not sincere: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
