

#calss header
class _UNBECOMING():
	def __init__(self,): 
		self.name = "UNBECOMING"
		self.definitions = [u'Unbecoming clothes do not look attractive on a particular person.', u'Unbecoming behaviour is not correct or not acceptable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
