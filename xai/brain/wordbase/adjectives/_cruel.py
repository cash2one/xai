

#calss header
class _CRUEL():
	def __init__(self,): 
		self.name = "CRUEL"
		self.definitions = [u'extremely unkind and unpleasant and causing pain to people or animals intentionally: ', u'causing suffering: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
