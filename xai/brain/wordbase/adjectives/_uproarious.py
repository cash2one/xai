

#calss header
class _UPROARIOUS():
	def __init__(self,): 
		self.name = "UPROARIOUS"
		self.definitions = [u'extremely noisy and confused: ', u'extremely funny: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
