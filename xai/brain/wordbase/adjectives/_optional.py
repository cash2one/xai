

#calss header
class _OPTIONAL():
	def __init__(self,): 
		self.name = "OPTIONAL"
		self.definitions = [u'If something is optional, you can choose if you want to do it, pay it, buy it, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
