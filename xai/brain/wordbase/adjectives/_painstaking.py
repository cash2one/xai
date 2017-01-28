

#calss header
class _PAINSTAKING():
	def __init__(self,): 
		self.name = "PAINSTAKING"
		self.definitions = [u'extremely careful and correct, and involving a lot of effort: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
