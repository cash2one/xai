

#calss header
class _TATTERED():
	def __init__(self,): 
		self.name = "TATTERED"
		self.definitions = [u'(especially of cloth or paper) badly torn: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
