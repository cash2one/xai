

#calss header
class _ADAPTABLE():
	def __init__(self,): 
		self.name = "ADAPTABLE"
		self.definitions = [u'able or willing to change in order to suit different conditions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
