

#calss header
class _TYPEWRITTEN():
	def __init__(self,): 
		self.name = "TYPEWRITTEN"
		self.definitions = [u'printed using a typewriter or computer: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
