

#calss header
class _ADRIFT():
	def __init__(self,): 
		self.name = "ADRIFT"
		self.definitions = [u'If a boat is adrift, it is moving on the water but is not controlled by anyone because of a problem: ', u'If a person is adrift, they do not have a clear purpose in life or know what they want to do: ', u'to become loose: ', u'If plans go adrift, they fail or do not produce the correct results: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
