

#calss header
class _ATTRIBUTABLE():
	def __init__(self,): 
		self.name = "ATTRIBUTABLE"
		self.definitions = [u'caused by: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
