

#calss header
class _WIDESPREAD():
	def __init__(self,): 
		self.name = "WIDESPREAD"
		self.definitions = [u'existing or happening in many places and/or among many people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
