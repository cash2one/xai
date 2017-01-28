

#calss header
class _INEXTINGUISHABLE():
	def __init__(self,): 
		self.name = "INEXTINGUISHABLE"
		self.definitions = [u'unable to be stopped from burning or existing']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
