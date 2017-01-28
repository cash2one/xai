

#calss header
class _TOTALITARIAN():
	def __init__(self,): 
		self.name = "TOTALITARIAN"
		self.definitions = [u'of or being a political system in which those in power have complete control and do not allow people freedom to oppose them: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
