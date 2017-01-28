

#calss header
class _DECIMAL():
	def __init__(self,): 
		self.name = "DECIMAL"
		self.definitions = [u'relating to or expressed in a system of counting based on the number ten: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
