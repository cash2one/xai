

#calss header
class _UNSPORTSMANLIKE():
	def __init__(self,): 
		self.name = "UNSPORTSMANLIKE"
		self.definitions = [u'not showing fairness or respect to other people, especially towards the opposing team or player when playing sport ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
