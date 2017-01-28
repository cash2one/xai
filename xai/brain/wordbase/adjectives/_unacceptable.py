

#calss header
class _UNACCEPTABLE():
	def __init__(self,): 
		self.name = "UNACCEPTABLE"
		self.definitions = [u'too bad to be accepted, approved of, or allowed to continue: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
