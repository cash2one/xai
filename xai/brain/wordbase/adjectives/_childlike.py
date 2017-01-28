

#calss header
class _CHILDLIKE():
	def __init__(self,): 
		self.name = "CHILDLIKE"
		self.definitions = [u'(of adults) showing the good qualities that children have, such as trusting people, being honest and enthusiastic: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
