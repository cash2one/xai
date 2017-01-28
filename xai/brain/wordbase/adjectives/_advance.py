

#calss header
class _ADVANCE():
	def __init__(self,): 
		self.name = "ADVANCE"
		self.definitions = [u'happening, done, or ready before an event: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
