

#calss header
class _BIRACIAL():
	def __init__(self,): 
		self.name = "BIRACIAL"
		self.definitions = [u'concerning or containing members of two different races: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
