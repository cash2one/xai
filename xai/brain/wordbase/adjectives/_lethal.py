

#calss header
class _LETHAL():
	def __init__(self,): 
		self.name = "LETHAL"
		self.definitions = [u'able to cause or causing death; extremely dangerous: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
