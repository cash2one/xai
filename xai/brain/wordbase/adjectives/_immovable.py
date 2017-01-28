

#calss header
class _IMMOVABLE():
	def __init__(self,): 
		self.name = "IMMOVABLE"
		self.definitions = [u'fixed and impossible to move: ', u'used to describe a firm opinion that is impossible to change, or someone with such an opinion']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
