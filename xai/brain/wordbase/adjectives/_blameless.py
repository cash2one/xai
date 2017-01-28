

#calss header
class _BLAMELESS():
	def __init__(self,): 
		self.name = "BLAMELESS"
		self.definitions = [u'not responsible for anything bad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
