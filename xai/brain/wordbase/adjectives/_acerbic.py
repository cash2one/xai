

#calss header
class _ACERBIC():
	def __init__(self,): 
		self.name = "ACERBIC"
		self.definitions = [u'used to describe something that is spoken or written in a way that is direct, clever, and cruel: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
