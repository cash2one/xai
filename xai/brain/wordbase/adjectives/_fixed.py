

#calss header
class _FIXED():
	def __init__(self,): 
		self.name = "FIXED"
		self.definitions = [u'arranged or decided already and not able to be changed: ', u'fastened somewhere and not able to be moved']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
