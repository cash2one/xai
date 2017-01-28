

#calss header
class _CLANDESTINE():
	def __init__(self,): 
		self.name = "CLANDESTINE"
		self.definitions = [u'planned or done in secret, especially describing something that is not officially allowed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
