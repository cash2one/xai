

#calss header
class _BLANKET():
	def __init__(self,): 
		self.name = "BLANKET"
		self.definitions = [u'including or affecting everything, everyone, or all cases, in a large group or area: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
