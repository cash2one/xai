

#calss header
class _UNSCRUPULOUS():
	def __init__(self,): 
		self.name = "UNSCRUPULOUS"
		self.definitions = [u'behaving in a way that is dishonest or unfair in order to get what you want: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
