

#calss header
class _REGULATORY():
	def __init__(self,): 
		self.name = "REGULATORY"
		self.definitions = [u'controlling: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
