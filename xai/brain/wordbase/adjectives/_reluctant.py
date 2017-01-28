

#calss header
class _RELUCTANT():
	def __init__(self,): 
		self.name = "RELUCTANT"
		self.definitions = [u'not willing to do something and therefore slow to do it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
