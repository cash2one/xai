

#calss header
class _DISTURBED():
	def __init__(self,): 
		self.name = "DISTURBED"
		self.definitions = [u'not thinking or behaving normally because of mental or emotional problems: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
