

#calss header
class _UNREPEATABLE():
	def __init__(self,): 
		self.name = "UNREPEATABLE"
		self.definitions = [u'An unrepeatable event, price, etc. cannot happen again: ', u'An unrepeatable word or remark used by another person is too rude or too difficult for you to repeat: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
