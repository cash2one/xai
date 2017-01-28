

#calss header
class _CONGRESSIONAL():
	def __init__(self,): 
		self.name = "CONGRESSIONAL"
		self.definitions = [u'belonging or related to the US Congress: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
