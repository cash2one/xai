

#calss header
class _CONVENTIONAL():
	def __init__(self,): 
		self.name = "CONVENTIONAL"
		self.definitions = [u'traditional and ordinary: ', u'used to refer to weapons that are not nuclear, or to methods of fighting a war that do not involve nuclear weapons: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
