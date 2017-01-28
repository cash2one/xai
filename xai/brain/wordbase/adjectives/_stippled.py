

#calss header
class _STIPPLED():
	def __init__(self,): 
		self.name = "STIPPLED"
		self.definitions = [u'drawn, painted, or coloured using small spots or marks: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
