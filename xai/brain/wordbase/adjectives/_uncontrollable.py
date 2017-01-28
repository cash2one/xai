

#calss header
class _UNCONTROLLABLE():
	def __init__(self,): 
		self.name = "UNCONTROLLABLE"
		self.definitions = [u'too strong or violent to be controlled: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
