

#calss header
class _UNRELIABLE():
	def __init__(self,): 
		self.name = "UNRELIABLE"
		self.definitions = [u'not able to be trusted or believed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
