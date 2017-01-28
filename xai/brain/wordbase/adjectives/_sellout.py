

#calss header
class _SELLOUT():
	def __init__(self,): 
		self.name = "SELLOUT"
		self.definitions = [u'A sellout performance or sports event has no more tickets available, because it is so popular: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
