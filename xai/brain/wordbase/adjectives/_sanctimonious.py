

#calss header
class _SANCTIMONIOUS():
	def __init__(self,): 
		self.name = "SANCTIMONIOUS"
		self.definitions = [u'acting as if morally better than others: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
