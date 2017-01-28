

#calss header
class _SKELETAL():
	def __init__(self,): 
		self.name = "SKELETAL"
		self.definitions = [u'of or like a skeleton (= frame of bones): ', u'used to describe something that exists in its most basic form: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
