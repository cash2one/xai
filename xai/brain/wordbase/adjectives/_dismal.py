

#calss header
class _DISMAL():
	def __init__(self,): 
		self.name = "DISMAL"
		self.definitions = [u'sad and without hope: ', u'very bad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
