

#calss header
class _VIGILANT():
	def __init__(self,): 
		self.name = "VIGILANT"
		self.definitions = [u'always being careful to notice things, especially possible danger: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
