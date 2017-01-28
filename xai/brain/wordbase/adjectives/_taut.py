

#calss header
class _TAUT():
	def __init__(self,): 
		self.name = "TAUT"
		self.definitions = [u'tight or completely stretched: ', u'excited or nervous: ', u'Taut writing or speech is controlled, clear, and short: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
