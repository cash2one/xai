

#calss header
class _ANTAGONISTIC():
	def __init__(self,): 
		self.name = "ANTAGONISTIC"
		self.definitions = [u'actively opposing or showing unfriendliness towards something or someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
