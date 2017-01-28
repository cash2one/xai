

#calss header
class _AMUSED():
	def __init__(self,): 
		self.name = "AMUSED"
		self.definitions = [u'showing that you think something is funny: ', u'to keep someone interested and help them to have an enjoyable time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
