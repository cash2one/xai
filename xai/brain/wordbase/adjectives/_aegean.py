

#calss header
class _AEGEAN():
	def __init__(self,): 
		self.name = "AEGEAN"
		self.definitions = [u'in or relating to the Aegean: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
