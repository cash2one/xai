

#calss header
class _POSH():
	def __init__(self,): 
		self.name = "POSH"
		self.definitions = [u'(of places and things) expensive and of high quality: ', u'(of people and their voices) from a high social class: ', u'used for describing a woman from a high social class who chooses to have a caesarean section (= a medical operation) to have her baby']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
