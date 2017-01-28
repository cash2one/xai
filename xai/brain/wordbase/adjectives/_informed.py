

#calss header
class _INFORMED():
	def __init__(self,): 
		self.name = "INFORMED"
		self.definitions = [u'having a lot of knowledge or information about something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
