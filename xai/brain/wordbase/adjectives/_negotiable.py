

#calss header
class _NEGOTIABLE():
	def __init__(self,): 
		self.name = "NEGOTIABLE"
		self.definitions = [u'able to be discussed or changed in order to reach an agreement: ', u'A cheque that is not negotiable cannot be exchanged for money and must be paid into a bank account.', u'A negotiable financial product is one that can be bought and sold: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
