

#calss header
class _MEMORIAL():
	def __init__(self,): 
		self.name = "MEMORIAL"
		self.definitions = [u'done to remember a person or people who have died: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
