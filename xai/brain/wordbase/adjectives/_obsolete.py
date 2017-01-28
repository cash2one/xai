

#calss header
class _OBSOLETE():
	def __init__(self,): 
		self.name = "OBSOLETE"
		self.definitions = [u'not in use any more, having been replaced by something newer and better or more fashionable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
