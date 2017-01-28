

#calss header
class _SCARED():
	def __init__(self,): 
		self.name = "SCARED"
		self.definitions = [u'frightened or worried: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
