

#calss header
class _DISPIRITED():
	def __init__(self,): 
		self.name = "DISPIRITED"
		self.definitions = [u'not feeling much hope about a particular situation or problem: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
