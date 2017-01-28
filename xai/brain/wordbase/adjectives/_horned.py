

#calss header
class _HORNED():
	def __init__(self,): 
		self.name = "HORNED"
		self.definitions = [u'A horned animal has horns: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
