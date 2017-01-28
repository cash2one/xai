

#calss header
class _MAXILLARY():
	def __init__(self,): 
		self.name = "MAXILLARY"
		self.definitions = [u'relating to the upper jaw: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
