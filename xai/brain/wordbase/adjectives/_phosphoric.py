

#calss header
class _PHOSPHORIC():
	def __init__(self,): 
		self.name = "PHOSPHORIC"
		self.definitions = [u'of or containing phosphorus: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
