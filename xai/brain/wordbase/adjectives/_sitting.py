

#calss header
class _SITTING():
	def __init__(self,): 
		self.name = "SITTING"
		self.definitions = [u'existing or continuing at the present time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
