

#calss header
class _AILING():
	def __init__(self,): 
		self.name = "AILING"
		self.definitions = [u'experiencing difficulty and problems: ', u'weak and suffering from illness: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
