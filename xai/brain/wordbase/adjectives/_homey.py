

#calss header
class _HOMEY():
	def __init__(self,): 
		self.name = "HOMEY"
		self.definitions = [u'plain or ordinary, but pleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
