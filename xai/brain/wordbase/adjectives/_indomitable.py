

#calss header
class _INDOMITABLE():
	def __init__(self,): 
		self.name = "INDOMITABLE"
		self.definitions = [u'used to say that someone is strong, brave, determined, and difficult to defeat or frighten: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
