

#calss header
class _DARWINIAN():
	def __init__(self,): 
		self.name = "DARWINIAN"
		self.definitions = [u'relating to the theories of Charles Darwin, which described how animals and plants change and develop over millions of years, with those that are best suited to their environment being the most successful and others that are less well suited not continuing to exist: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
