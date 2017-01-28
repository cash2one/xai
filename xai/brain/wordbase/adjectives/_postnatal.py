

#calss header
class _POSTNATAL():
	def __init__(self,): 
		self.name = "POSTNATAL"
		self.definitions = [u'relating to the period of time immediately after a baby has been born: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
