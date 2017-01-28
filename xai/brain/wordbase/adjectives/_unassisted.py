

#calss header
class _UNASSISTED():
	def __init__(self,): 
		self.name = "UNASSISTED"
		self.definitions = [u'without being helped by anyone or anything: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
