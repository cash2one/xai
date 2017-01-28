

#calss header
class _RENTED():
	def __init__(self,): 
		self.name = "RENTED"
		self.definitions = [u'used to refer to something that you rent: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
