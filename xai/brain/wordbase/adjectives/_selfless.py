

#calss header
class _SELFLESS():
	def __init__(self,): 
		self.name = "SELFLESS"
		self.definitions = [u'caring more for what other people need and want rather than for what you yourself need and want: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
