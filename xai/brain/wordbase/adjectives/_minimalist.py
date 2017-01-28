

#calss header
class _MINIMALIST():
	def __init__(self,): 
		self.name = "MINIMALIST"
		self.definitions = [u'belonging or relating to a style in art, design, and theatre that uses the smallest range of materials and colours possible, and only very simple shapes or forms: ', u'taking or showing as little action and involvement in a situation as possible: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
