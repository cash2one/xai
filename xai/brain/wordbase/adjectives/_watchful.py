

#calss header
class _WATCHFUL():
	def __init__(self,): 
		self.name = "WATCHFUL"
		self.definitions = [u'paying careful attention and ready to deal with problems: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
