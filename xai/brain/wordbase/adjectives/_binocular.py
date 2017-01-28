

#calss header
class _BINOCULAR():
	def __init__(self,): 
		self.name = "BINOCULAR"
		self.definitions = [u'using both eyes to see things; made for use with both eyes: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
