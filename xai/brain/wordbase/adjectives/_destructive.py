

#calss header
class _DESTRUCTIVE():
	def __init__(self,): 
		self.name = "DESTRUCTIVE"
		self.definitions = [u'causing, or able to cause, damage: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
