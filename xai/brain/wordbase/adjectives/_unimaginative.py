

#calss header
class _UNIMAGINATIVE():
	def __init__(self,): 
		self.name = "UNIMAGINATIVE"
		self.definitions = [u'not new, original, or clever; not showing any imagination']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
