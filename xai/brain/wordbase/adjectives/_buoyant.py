

#calss header
class _BUOYANT():
	def __init__(self,): 
		self.name = "BUOYANT"
		self.definitions = [u'able to float: ', u'happy and confident: ', u'successful or making a profit: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
