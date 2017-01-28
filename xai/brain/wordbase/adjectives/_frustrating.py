

#calss header
class _FRUSTRATING():
	def __init__(self,): 
		self.name = "FRUSTRATING"
		self.definitions = [u'making you feel annoyed or less confident because you cannot achieve what you want: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
