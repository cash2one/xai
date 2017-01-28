

#calss header
class _UNSWERVING():
	def __init__(self,): 
		self.name = "UNSWERVING"
		self.definitions = [u"If someone's trust or belief is unswerving, it is always strong and never becomes weaker: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
