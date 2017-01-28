

#calss header
class _UNCTUOUS():
	def __init__(self,): 
		self.name = "UNCTUOUS"
		self.definitions = [u'Unctuous people or behaviour expresses too much praise, interest, friendliness, etc., in a way that is false and unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
