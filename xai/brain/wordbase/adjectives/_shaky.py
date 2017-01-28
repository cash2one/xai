

#calss header
class _SHAKY():
	def __init__(self,): 
		self.name = "SHAKY"
		self.definitions = [u'moving with quick, short movements from side to side, not in a controlled way: ', u'upset: ', u'not firm or strong: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
