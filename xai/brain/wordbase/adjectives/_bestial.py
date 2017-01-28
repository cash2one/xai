

#calss header
class _BESTIAL():
	def __init__(self,): 
		self.name = "BESTIAL"
		self.definitions = [u'cruel or like an animal: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
