

#calss header
class _ORBITAL():
	def __init__(self,): 
		self.name = "ORBITAL"
		self.definitions = [u'relating to the orbit (= curved path) of an object in space: ', u'relating to the eye socket (= the bone around the eye)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
