

#calss header
class _UNTOUCHED():
	def __init__(self,): 
		self.name = "UNTOUCHED"
		self.definitions = [u'not changed or spoiled in any way: ', u'If food is untouched, it has not been eaten: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
