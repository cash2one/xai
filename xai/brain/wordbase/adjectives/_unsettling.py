

#calss header
class _UNSETTLING():
	def __init__(self,): 
		self.name = "UNSETTLING"
		self.definitions = [u'causing change', u'causing worry or anxiety: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
