

#calss header
class _UNCHARITABLE():
	def __init__(self,): 
		self.name = "UNCHARITABLE"
		self.definitions = [u'unkind and unfair: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
