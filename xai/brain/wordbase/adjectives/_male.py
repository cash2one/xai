

#calss header
class _MALE():
	def __init__(self,): 
		self.name = "MALE"
		self.definitions = [u'used to refer to men or boys, or the sex that fertilizes eggs, and does not produce babies or eggs itself: ', u'used to refer to a piece of equipment that has a part that sticks out and can be fitted into a hollow part in another piece of equipment: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
