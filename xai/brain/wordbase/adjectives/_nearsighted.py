

#calss header
class _NEARSIGHTED():
	def __init__(self,): 
		self.name = "NEARSIGHTED"
		self.definitions = [u'Someone who is nearsighted cannot see objects clearly that are far away.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
