

#calss header
class _AUTHORITARIAN():
	def __init__(self,): 
		self.name = "AUTHORITARIAN"
		self.definitions = [u'demanding that people obey completely and refusing to allow them freedom to act as they wish: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
