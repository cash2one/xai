

#calss header
class _STOCK():
	def __init__(self,): 
		self.name = "STOCK"
		self.definitions = [u'(of an idea, expression, or action) usual or typical, and used or done so many times that it is no longer original: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
