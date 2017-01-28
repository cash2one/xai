

#calss header
class _ADDICTED():
	def __init__(self,): 
		self.name = "ADDICTED"
		self.definitions = [u'unable to stop taking drugs, or doing something as a habit: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
