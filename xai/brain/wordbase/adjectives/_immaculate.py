

#calss header
class _IMMACULATE():
	def __init__(self,): 
		self.name = "IMMACULATE"
		self.definitions = [u'perfectly clean or tidy: ', u'perfect and without any mistakes: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
