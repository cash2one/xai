

#calss header
class _NORTHEASTERN():
	def __init__(self,): 
		self.name = "NORTHEASTERN"
		self.definitions = [u'in or from the northeast: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
