

#calss header
class _INTERLOCKING():
	def __init__(self,): 
		self.name = "INTERLOCKING"
		self.definitions = [u'firmly joined together, especially by one part fitting into another: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
