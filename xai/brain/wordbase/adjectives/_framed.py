

#calss header
class _FRAMED():
	def __init__(self,): 
		self.name = "FRAMED"
		self.definitions = [u'surrounded by a border: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
