

#calss header
class _APPROVING():
	def __init__(self,): 
		self.name = "APPROVING"
		self.definitions = [u'showing that you have a positive opinion about something or someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
