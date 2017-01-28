

#calss header
class _MODERNIST():
	def __init__(self,): 
		self.name = "MODERNIST"
		self.definitions = [u'relating to or a member of the modern art movement: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
