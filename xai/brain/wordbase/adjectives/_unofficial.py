

#calss header
class _UNOFFICIAL():
	def __init__(self,): 
		self.name = "UNOFFICIAL"
		self.definitions = [u'not official; not from a person in authority, the government, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
