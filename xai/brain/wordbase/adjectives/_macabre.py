

#calss header
class _MACABRE():
	def __init__(self,): 
		self.name = "MACABRE"
		self.definitions = [u'used to describe something that is very strange and unpleasant because it is connected with death or violence: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
