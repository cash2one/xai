

#calss header
class _AVERAGE():
	def __init__(self,): 
		self.name = "AVERAGE"
		self.definitions = [u'An average number is the number you get by adding two or more amounts together and dividing the total by the number of amounts: ', u'typical and usual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
