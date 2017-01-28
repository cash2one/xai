

#calss header
class _FEMALE():
	def __init__(self,): 
		self.name = "FEMALE"
		self.definitions = [u'belonging or relating to women, or the sex that can give birth to young or produce eggs: ', u'Female plants produce flowers that will later develop into fruit.', u'used to refer to a piece of equipment that has a hole or space into which another part can be fitted: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
