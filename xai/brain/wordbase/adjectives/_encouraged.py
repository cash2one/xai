

#calss header
class _ENCOURAGED():
	def __init__(self,): 
		self.name = "ENCOURAGED"
		self.definitions = [u'having more confidence or hope about something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
