

#calss header
class _SMOKY():
	def __init__(self,): 
		self.name = "SMOKY"
		self.definitions = [u'If a place is smoky, there is a lot of smoke in it: ', u'similar to smoke: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
