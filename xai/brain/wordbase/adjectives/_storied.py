

#calss header
class _STORIED():
	def __init__(self,): 
		self.name = "STORIED"
		self.definitions = [u'often spoken of or written about: ', u'having the stated number of stories (= levels): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
