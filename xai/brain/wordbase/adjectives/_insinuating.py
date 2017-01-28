

#calss header
class _INSINUATING():
	def __init__(self,): 
		self.name = "INSINUATING"
		self.definitions = [u'suggesting ideas without saying them directly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
