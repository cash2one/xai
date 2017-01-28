

#calss header
class _DISTRESSED():
	def __init__(self,): 
		self.name = "DISTRESSED"
		self.definitions = [u'upset or worried: ', u'having problems because of having too little money: ', u'a distressed material has been treated to make it look as if it has been used for a long time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
