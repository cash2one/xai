

#calss header
class _FREEWHEELING():
	def __init__(self,): 
		self.name = "FREEWHEELING"
		self.definitions = [u'not limited by rules or accepted ways of doing things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
