

#calss header
class _AGAPE():
	def __init__(self,): 
		self.name = "AGAPE"
		self.definitions = [u'with the mouth open, especially showing surprise or shock: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
