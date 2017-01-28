

#calss header
class _CRANKY():
	def __init__(self,): 
		self.name = "CRANKY"
		self.definitions = [u'easily annoyed or upset: ', u'strange and unusual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
