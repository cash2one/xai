

#calss header
class _DISMISSIVE():
	def __init__(self,): 
		self.name = "DISMISSIVE"
		self.definitions = [u'showing that you do not think something is worth considering: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
