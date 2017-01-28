

#calss header
class _PRESHRUNK():
	def __init__(self,): 
		self.name = "PRESHRUNK"
		self.definitions = [u'(of clothes) shrunk (= made smaller) by washing before being sold: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
