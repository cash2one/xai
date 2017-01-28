

#calss header
class _SPARSE():
	def __init__(self,): 
		self.name = "SPARSE"
		self.definitions = [u'small in numbers or amount, often spread over a large area: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
