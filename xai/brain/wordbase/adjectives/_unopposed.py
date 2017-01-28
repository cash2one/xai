

#calss header
class _UNOPPOSED():
	def __init__(self,): 
		self.name = "UNOPPOSED"
		self.definitions = [u'with no one trying to compete against you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
