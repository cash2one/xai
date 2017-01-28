

#calss header
class _PAYABLE():
	def __init__(self,): 
		self.name = "PAYABLE"
		self.definitions = [u'that should be paid: ', u'If a cheque is payable to a particular person or organization, his, her, or its name is written on it and the money will be paid to him, her, or it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
