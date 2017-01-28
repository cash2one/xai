

#calss header
class _PRESENT():
	def __init__(self,): 
		self.name = "PRESENT"
		self.definitions = [u'in a particular place: ', u'happening or existing now: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
