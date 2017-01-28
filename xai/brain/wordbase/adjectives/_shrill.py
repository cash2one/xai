

#calss header
class _SHRILL():
	def __init__(self,): 
		self.name = "SHRILL"
		self.definitions = [u'having a loud and high sound that is unpleasant or painful to listen to: ', u'used to describe a way of arguing or criticizing that seems too forceful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
