

#calss header
class _INADVERTENT():
	def __init__(self,): 
		self.name = "INADVERTENT"
		self.definitions = [u'not intentional: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
