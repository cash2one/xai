

#calss header
class _LACY():
	def __init__(self,): 
		self.name = "LACY"
		self.definitions = [u'made of or decorated with lace (= decorative cloth): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
