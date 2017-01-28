

#calss header
class _TELLING():
	def __init__(self,): 
		self.name = "TELLING"
		self.definitions = [u'showing the truth about a situation or showing what someone really thinks: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
