

#calss header
class _LEATHERY():
	def __init__(self,): 
		self.name = "LEATHERY"
		self.definitions = [u'with the look and feel of leather: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
