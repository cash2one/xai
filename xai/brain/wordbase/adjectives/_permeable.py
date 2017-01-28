

#calss header
class _PERMEABLE():
	def __init__(self,): 
		self.name = "PERMEABLE"
		self.definitions = [u'If a substance is permeable, it allows liquids or gases to go through it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
