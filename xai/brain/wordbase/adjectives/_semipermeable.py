

#calss header
class _SEMIPERMEABLE():
	def __init__(self,): 
		self.name = "SEMIPERMEABLE"
		self.definitions = [u'Something, for example a cell membrane, that is semipermeable allows some liquids and gases to pass through it, but not others.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
