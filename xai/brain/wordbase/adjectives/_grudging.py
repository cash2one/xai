

#calss header
class _GRUDGING():
	def __init__(self,): 
		self.name = "GRUDGING"
		self.definitions = [u'A grudging action or feeling is one that you do or have unwillingly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
