

#calss header
class _BREAKNECK():
	def __init__(self,): 
		self.name = "BREAKNECK"
		self.definitions = [u'carelessly fast and dangerous: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
