

#calss header
class _AUTOMATIC():
	def __init__(self,): 
		self.name = "AUTOMATIC"
		self.definitions = [u'An automatic machine or device is able to operate independently of human control: ', u'done without thinking about it: ', u'certain to happen as part of the normal process or system: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
