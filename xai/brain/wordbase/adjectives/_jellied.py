

#calss header
class _JELLIED():
	def __init__(self,): 
		self.name = "JELLIED"
		self.definitions = [u'Jellied meat or fish is cooked and then served in its own juices that become firm when cold: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
