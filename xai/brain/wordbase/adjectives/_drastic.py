

#calss header
class _DRASTIC():
	def __init__(self,): 
		self.name = "DRASTIC"
		self.definitions = [u'(especially of actions) severe and sudden or having very noticeable effects: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
