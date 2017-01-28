

#calss header
class _MINISTERIAL():
	def __init__(self,): 
		self.name = "MINISTERIAL"
		self.definitions = [u'relating to or involving a minister (= an important member of the government): ', u'relating to or involving a minister who represents his or her country in another country: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
