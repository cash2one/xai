

#calss header
class _MOONLIT():
	def __init__(self,): 
		self.name = "MOONLIT"
		self.definitions = [u'able to be seen because of the light of the moon: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
