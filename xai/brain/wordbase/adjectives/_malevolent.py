

#calss header
class _MALEVOLENT():
	def __init__(self,): 
		self.name = "MALEVOLENT"
		self.definitions = [u'causing or wanting to cause harm or evil: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
