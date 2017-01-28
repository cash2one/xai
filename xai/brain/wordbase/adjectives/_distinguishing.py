

#calss header
class _DISTINGUISHING():
	def __init__(self,): 
		self.name = "DISTINGUISHING"
		self.definitions = [u'A distinguishing mark or feature is one that makes someone or something different from similar people or things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
