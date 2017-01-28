

#calss header
class _REBORN():
	def __init__(self,): 
		self.name = "REBORN"
		self.definitions = [u'existing or active again : ', u'having decided to accept a particular type of evangelical Christianity, especially after a deep spiritual experience : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
