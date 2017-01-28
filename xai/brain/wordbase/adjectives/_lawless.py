

#calss header
class _LAWLESS():
	def __init__(self,): 
		self.name = "LAWLESS"
		self.definitions = [u'not controlled by laws, or illegal: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
