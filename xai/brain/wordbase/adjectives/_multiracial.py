

#calss header
class _MULTIRACIAL():
	def __init__(self,): 
		self.name = "MULTIRACIAL"
		self.definitions = [u'involving people of several different races: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
