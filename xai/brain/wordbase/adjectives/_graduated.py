

#calss header
class _GRADUATED():
	def __init__(self,): 
		self.name = "GRADUATED"
		self.definitions = [u'divided into levels or stages: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
