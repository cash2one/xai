

#calss header
class _JACOBEAN():
	def __init__(self,): 
		self.name = "JACOBEAN"
		self.definitions = [u'relating to the period from 1603 to 1625 when James I was king of England: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
