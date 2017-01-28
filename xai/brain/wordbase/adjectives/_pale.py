

#calss header
class _PALE():
	def __init__(self,): 
		self.name = "PALE"
		self.definitions = [u"used to describe a person's face or skin if it has less colour than usual, for example when the person is or ill or frightened, or if it has less colour than people generally have: ", u'A pale light or colour is not bright or strong: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
