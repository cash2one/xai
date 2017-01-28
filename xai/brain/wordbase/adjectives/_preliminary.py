

#calss header
class _PRELIMINARY():
	def __init__(self,): 
		self.name = "PRELIMINARY"
		self.definitions = [u'coming before a more important action or event, especially introducing or preparing for it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
