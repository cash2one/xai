

#calss header
class _RUMOURED():
	def __init__(self,): 
		self.name = "RUMOURED"
		self.definitions = [u'used to refer to a fact or piece of news that might be true or invented, and quickly spreads from person to person: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
