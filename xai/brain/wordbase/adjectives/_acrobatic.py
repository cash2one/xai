

#calss header
class _ACROBATIC():
	def __init__(self,): 
		self.name = "ACROBATIC"
		self.definitions = [u'involving or able to perform difficult and attractive body movements: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
