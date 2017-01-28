

#calss header
class _STIFLING():
	def __init__(self,): 
		self.name = "STIFLING"
		self.definitions = [u'extremely hot and unpleasant: ', u'preventing something from happening: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
