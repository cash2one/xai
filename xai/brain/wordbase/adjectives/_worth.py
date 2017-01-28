

#calss header
class _WORTH():
	def __init__(self,): 
		self.name = "WORTH"
		self.definitions = [u'having a particular value, especially in money: ', u'having a particular amount of money: ', u'to be of reasonable or good value for the price: ', u'to be important or interesting enough to receive a particular action: ', u'to be important or useful to have or do: ', u'enjoyable enough or producing enough advantages to make the necessary effort, risk, pain, etc. seem acceptable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
