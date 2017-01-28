

#calss header
class _AZURE():
	def __init__(self,): 
		self.name = "AZURE"
		self.definitions = [u'having the bright blue colour of the sky on a clear day: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
