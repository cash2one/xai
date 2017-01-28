

#calss header
class _NOSTALGIC():
	def __init__(self,): 
		self.name = "NOSTALGIC"
		self.definitions = [u'feeling happy and also slightly sad when you think about things that happened in the past: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
