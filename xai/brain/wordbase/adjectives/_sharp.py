

#calss header
class _SHARP():
	def __init__(self,): 
		self.name = "SHARP"
		self.definitions = [u'higher than the correct or stated musical note: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
