

#calss header
class _REGRETTABLE():
	def __init__(self,): 
		self.name = "REGRETTABLE"
		self.definitions = [u'making you feel sad and sorry about something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
