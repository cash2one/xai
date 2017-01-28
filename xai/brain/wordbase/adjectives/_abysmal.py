

#calss header
class _ABYSMAL():
	def __init__(self,): 
		self.name = "ABYSMAL"
		self.definitions = [u'very bad: ', u'very deep: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
