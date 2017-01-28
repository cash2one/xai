

#calss header
class _AMBITIOUS():
	def __init__(self,): 
		self.name = "AMBITIOUS"
		self.definitions = [u'having a strong wish to be successful, powerful, or rich: ', u'If a plan or idea is ambitious, it needs a great amount of skill and effort to be successful or be achieved: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
