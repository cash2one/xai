

#calss header
class _NEGLECTED():
	def __init__(self,): 
		self.name = "NEGLECTED"
		self.definitions = [u'not receiving enough care or attention: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
