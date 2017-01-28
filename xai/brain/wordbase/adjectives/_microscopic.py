

#calss header
class _MICROSCOPIC():
	def __init__(self,): 
		self.name = "MICROSCOPIC"
		self.definitions = [u'very small and only able to be seen with a microscope: ', u'extremely small: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
