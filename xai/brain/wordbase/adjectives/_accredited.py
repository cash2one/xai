

#calss header
class _ACCREDITED():
	def __init__(self,): 
		self.name = "ACCREDITED"
		self.definitions = [u'officially recognized or approved: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
