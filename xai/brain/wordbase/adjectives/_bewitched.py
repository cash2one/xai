

#calss header
class _BEWITCHED():
	def __init__(self,): 
		self.name = "BEWITCHED"
		self.definitions = [u'extremely attracted to something, or completely controlled by something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
