

#calss header
class _PERISHING():
	def __init__(self,): 
		self.name = "PERISHING"
		self.definitions = [u'extremely cold: ', u'used to show your anger about something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
