

#calss header
class _CHEAP():
	def __init__(self,): 
		self.name = "CHEAP"
		self.definitions = [u'costing little money or less than is usual or expected: ', u'If a shop or restaurant is cheap, it charges low prices: ', u'cheap but good or enjoyable: ', u'If you get goods on the cheap, you get them for a low price, often from someone you know who works in the company or business that produces them.', u'used to describe goods that are both low in quality and low in price: ', u'costing little and of very bad quality', u'unwilling to spend money: ', u'If you describe the way a person is dressed as cheap, you mean that it is very obvious that they are trying to sexually attract other people.', u'unpleasant and unkind: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
