

#calss header
class _EQUITABLE():
	def __init__(self,): 
		self.name = "EQUITABLE"
		self.definitions = [u'treating everyone fairly and in the same way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
