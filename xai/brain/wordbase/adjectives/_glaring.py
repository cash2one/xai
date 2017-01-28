

#calss header
class _GLARING():
	def __init__(self,): 
		self.name = "GLARING"
		self.definitions = [u'used to say that something bad is very obvious: ', u'shining too brightly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
