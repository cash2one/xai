

#calss header
class _BROADCAST():
	def __init__(self,): 
		self.name = "BROADCAST"
		self.definitions = [u'A broadcast station is a television station sent out from the ground rather than using satellites.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
