

#calss header
class _JUBILANT():
	def __init__(self,): 
		self.name = "JUBILANT"
		self.definitions = [u'feeling or expressing great happiness, especially because of a success: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
