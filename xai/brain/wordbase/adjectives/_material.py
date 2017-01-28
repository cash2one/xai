

#calss header
class _MATERIAL():
	def __init__(self,): 
		self.name = "MATERIAL"
		self.definitions = [u'relating to physical objects or money rather than emotions or the spiritual world: ', u'important or having an important effect: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
