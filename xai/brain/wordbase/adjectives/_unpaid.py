

#calss header
class _UNPAID():
	def __init__(self,): 
		self.name = "UNPAID"
		self.definitions = [u'An unpaid debt, tax, etc. has not been paid: ', u'Unpaid work is work that you do without getting any money for it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
