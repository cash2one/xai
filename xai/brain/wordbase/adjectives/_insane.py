

#calss header
class _INSANE():
	def __init__(self,): 
		self.name = "INSANE"
		self.definitions = [u'mentally ill: ', u'extremely unreasonable or stupid: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
