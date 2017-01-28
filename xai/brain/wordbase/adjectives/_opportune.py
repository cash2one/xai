

#calss header
class _OPPORTUNE():
	def __init__(self,): 
		self.name = "OPPORTUNE"
		self.definitions = [u'happening at a time that is likely to produce success or is convenient: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
