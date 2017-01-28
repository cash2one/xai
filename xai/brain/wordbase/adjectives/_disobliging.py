

#calss header
class _DISOBLIGING():
	def __init__(self,): 
		self.name = "DISOBLIGING"
		self.definitions = [u'unwilling to help or do what you are asked to do']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
