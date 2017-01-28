

#calss header
class _HOUSEBROKEN():
	def __init__(self,): 
		self.name = "HOUSEBROKEN"
		self.definitions = [u'(of a pet) having learned not to urinate or empty its bowels in your home']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
