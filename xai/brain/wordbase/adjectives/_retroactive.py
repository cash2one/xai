

#calss header
class _RETROACTIVE():
	def __init__(self,): 
		self.name = "RETROACTIVE"
		self.definitions = [u'If a law or decision, etc. is retroactive, it has effect from a date before it was approved: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
