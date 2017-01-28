

#calss header
class _PREHENSILE():
	def __init__(self,): 
		self.name = "PREHENSILE"
		self.definitions = [u'(of parts of the body) able to hold on to things, especially by curling around them: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
