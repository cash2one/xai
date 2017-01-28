

#calss header
class _TRAGIC():
	def __init__(self,): 
		self.name = "TRAGIC"
		self.definitions = [u'very sad, often involving death and suffering: ', u'belonging or relating to literature about death or suffering: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
