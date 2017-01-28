

#calss header
class _UNIVERSAL():
	def __init__(self,): 
		self.name = "UNIVERSAL"
		self.definitions = [u'existing everywhere or involving everyone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
