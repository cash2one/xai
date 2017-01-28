

#calss header
class _IMPACTED():
	def __init__(self,): 
		self.name = "IMPACTED"
		self.definitions = [u'An impacted tooth cannot grow in the right way, usually because it is growing against another tooth below the gum.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
