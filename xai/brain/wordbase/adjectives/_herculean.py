

#calss header
class _HERCULEAN():
	def __init__(self,): 
		self.name = "HERCULEAN"
		self.definitions = [u'needing great strength and determination: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
